import os
import json
import time
from typing import List

from uhashring import HashRing

from fastapi_crawler_scheduler.dbRedisHelper import redis_db
from config import settings
from utils.spiderSchedular import scheduler
from utils.crawlerScheduler import crawl_sitemap, crawl_twitter, crawl_latest_news

setp = 200


def div_list(tem_lists: List[any]) -> list:
    back_lists = list()
    tem_num = len(tem_lists)
    end_num = int(tem_num / setp)
    for i in range(end_num):
        ss = tem_lists[i * setp:(i + 1) * setp]
        back_lists.append(ss)
    back_lists.append(tem_lists[end_num * setp:])
    return back_lists


def scheduler_add_job(apscheduler_id: str, crawler_info: dict) -> None:
    if apscheduler_id.startswith('sitemap'):
        func = crawl_sitemap
    elif apscheduler_id.startswith('latest_news'):
        func = crawl_latest_news
    elif apscheduler_id.startswith('twitter'):
        func = crawl_twitter
    else:
        return
    scheduler.add_job(
        func,
        id=apscheduler_id,
        name=apscheduler_id,
        trigger="interval",
        kwargs=crawler_info,
        seconds=30,
    )


class NewsScheduler(object):

    def __init__(self) -> None:
        self.process_id_list = []

    def check_process(self) -> None:
        redis_db.process_acquire(f'node:{settings.uuid_number}:{os.getpid()}')

    def get_process_list(self) -> list:
        return redis_db.get_proces_info()

    def process_check_count(self, process_id: int, check_key: str) -> None:
        if process_id not in self.process_id_list:
            if redis_db.acquire(lock_name=check_key):
                check_value = redis_db.from_key_get_value(key_name=check_key)
                if check_value is None:
                    return None
                check_process_number = check_value.get('check_process_number')
                if check_process_number is None:
                    check_process_number = 1
                else:
                    check_process_number += 1
                if check_process_number >= 2:
                    redis_db.delete_key(lock_name=check_key)
                else:
                    check_value['check_process_number'] = check_process_number
                    redis_db.string_set(key=check_key, value=json.dumps(check_value, ensure_ascii=False))
                redis_db.release(lock_name=check_key)

    def check_backend_task(self) -> None:
        node_process_id_list = self.get_process_list()
        self.process_id_list = [int(str(node_id).strip().split(':')[-1]) for node_id in node_process_id_list]
        # 处理后端操作
        hr = HashRing(nodes=node_process_id_list)
        backend_task = redis_db.get_backend_task()
        backend_key_list = div_list(tem_lists=backend_task)
        for key_list in backend_key_list:
            for backend_key, backend_info in redis_db.get_tasks(keys=key_list).items():
                if backend_info is None:
                    continue
                lock_all_backend_key = f'{redis_db.prefix}:all:{backend_info["apscheduler_id"]}'
                all_backend_key = f'all:{backend_info["apscheduler_id"]}'
                if not redis_db.lock_exists(lock_name=lock_all_backend_key):
                    process_node_id = hr.get_node(backend_info["apscheduler_id"])
                    backend_info['process_node_id'] = process_node_id
                    redis_db.string_set(key=all_backend_key, value=json.dumps(backend_info, ensure_ascii=False))
                    redis_db.delete_key(lock_name=backend_key)

    def check_all_task(self) -> None:
        node_process_id_list = self.get_process_list()
        self.process_id_list = [int(str(node_id).strip().split(':')[-1]) for node_id in node_process_id_list]
        hr = HashRing(nodes=node_process_id_list)
        # 处理 all_task
        all_task = redis_db.get_all_task()
        all_task_key_list = div_list(tem_lists=all_task)
        for key_list in all_task_key_list:
            for all_key, all_value in redis_db.get_tasks(keys=key_list).items():
                if redis_db.acquire(lock_name=all_key):
                    if all_value is None:
                        continue
                    redis_process_node_id = all_value["process_node_id"]
                    new_process_node_id = hr.get_node(all_value["apscheduler_id"])
                    if new_process_node_id == redis_process_node_id:
                        process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                        # 进程没变化
                        if all_value['is_change'] == 1:
                            next_key = f'{all_value["operation"]}:{settings.uuid_number}:{all_value["apscheduler_id"]}:{process_id}'
                            redis_db.string_set(key=next_key, value=json.dumps(all_value, ensure_ascii=False))
                            all_value["is_change"] = 0
                            redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                        else:
                            pass
                    else:
                        # 进程有变化
                        new_process_id = int(str(new_process_node_id).strip().split(':')[-1])
                        redis_process_id = int(str(redis_process_node_id).strip().split(':')[-1])
                        delete_key = f'delete:{settings.uuid_number}:{all_value["apscheduler_id"]}:{redis_process_id}'
                        all_value["details"] = "删除任务"
                        redis_db.string_set(key=delete_key, value=json.dumps(all_value, ensure_ascii=False))
                        all_value["process_node_id"] = new_process_node_id
                        if all_value['operation'] == 'delete':
                            # 无需向下一步添加任务
                            pass
                        else:
                            insert_key = f'insert:{settings.uuid_number}:{all_value["apscheduler_id"]}:{new_process_id}'
                            all_value["details"] = "进程变化，新增任务"
                            redis_db.string_set(key=insert_key, value=json.dumps(all_value, ensure_ascii=False))

                        all_value["is_change"] = 0
                        redis_db.string_set(key=all_key, value=json.dumps(all_value, ensure_ascii=False))
                    redis_db.release(lock_name=all_key)

    def check_insert_task(self) -> None:
        # 处理 insert_task
        insert_task = redis_db.get_insert_task()
        insert_task_key_list = div_list(tem_lists=insert_task)
        for key_list in insert_task_key_list:
            for insert_key, insert_value in redis_db.get_tasks(keys=key_list).items():
                if insert_value is None:
                    continue
                process_node_id = insert_value['process_node_id']
                apscheduler_id = insert_value['apscheduler_id']
                process_id = int(str(process_node_id).strip().split(':')[-1])
                if os.getpid() == process_id:
                    if scheduler.get_job(job_id=apscheduler_id):
                        scheduler.remove_job(job_id=apscheduler_id)
                    scheduler_add_job(apscheduler_id=apscheduler_id, crawler_info=insert_value)
                    redis_db.delete_key(lock_name=insert_key)
                else:
                    self.process_check_count(process_id=process_id, check_key=insert_key)

    def check_update_task(self) -> None:
        # 处理 update_task
        update_task = redis_db.get_update_task()
        update_task_key_list = div_list(tem_lists=update_task)
        for key_list in update_task_key_list:
            for update_key, update_value in redis_db.get_tasks(keys=key_list).items():
                if update_value is None:
                    continue
                process_node_id = update_value['process_node_id']
                apscheduler_id = update_value['apscheduler_id']
                process_id = int(str(process_node_id).strip().split(':')[-1])
                if os.getpid() == process_id:
                    if scheduler.get_job(job_id=apscheduler_id):
                        scheduler.remove_job(job_id=apscheduler_id)
                    scheduler_add_job(apscheduler_id=apscheduler_id, crawler_info=update_value)
                    redis_db.delete_key(lock_name=update_key)
                else:
                    self.process_check_count(process_id=process_id, check_key=update_key)

    def check_delete_task(self) -> None:
        # 处理 delete_task
        delete_task = redis_db.get_delete_task()
        delete_task_key_list = div_list(tem_lists=delete_task)
        for key_list in delete_task_key_list:
            for delete_key, delete_value in redis_db.get_tasks(keys=key_list).items():
                if delete_value is None:
                    continue
                process_node_id = delete_value['process_node_id']
                apscheduler_id = delete_value['apscheduler_id']
                process_id = int(str(process_node_id).strip().split(':')[-1])
                if os.getpid() == process_id:
                    if scheduler.get_job(job_id=apscheduler_id):
                        scheduler.remove_job(job_id=apscheduler_id)
                    redis_db.delete_key(lock_name=delete_key)
                    redis_db.delete_key(lock_name=f"scheduler_job:{apscheduler_id}")
                else:
                    self.process_check_count(process_id=process_id, check_key=delete_key)

    def insert_or_update_backend_task(self, operation: str, crawler_type: str, crawler_info: dict) -> dict:
        if operation in ['insert', 'update']:
            crawler_info['operation'] = operation
        else:
            return {"is_ok": 0, "reason": "operation 传参错误，['insert', 'update']"}
        if not crawler_info.get('id'):
            return {"is_ok": 0, "reason": "crawler_info 缺少 id"}
        if crawler_type in ['sitemap', 'latest_news', 'twitter']:
            crawler_info['apscheduler_id'] = f'{crawler_type}:{crawler_info.get("id")}'
        else:
            return {"is_ok": 0, "reason": "crawler_type 传参错误，['sitemap', 'latest_news', 'twitter']"}
        crawler_info['is_change'] = 1
        redis_db.string_set(f'backend:{crawler_type}:{crawler_info.get("id")}',
                            json.dumps(crawler_info, ensure_ascii=False))
        return {"is_ok": 1, "reason": f"success {crawler_type}_{crawler_info.get('id')}"}

    def delete_backend_task(self, crawler_type: str, crawler_id: int) -> dict:
        crawler_info = dict()
        if crawler_type in ['sitemap', 'latest_news', 'twitter']:
            crawler_info['apscheduler_id'] = f'{crawler_type}:{crawler_id}'
        else:
            return {"is_ok": 0, "reason": "crawler_type 传参错误，['sitemap', 'latest_news', 'twitter']"}
        crawler_info['is_change'] = 1
        crawler_info['operation'] = 'delete'
        redis_db.string_set(f'backend:{crawler_type}:{crawler_id}',
                            json.dumps(crawler_info, ensure_ascii=False))
        return {"is_ok": 1, "reason": f"success {crawler_type}_{crawler_id}"}

    def sync_scheduler_job_to_redis(self) -> None:
        job_list = scheduler.get_jobs()
        for job in job_list:
            key = f"scheduler_job:{job.id}"
            redis_db.process_acquire(lock_name=key, expire_time=300)

    def run(self) -> None:
        start_time = time.time()
        self.check_backend_task()
        self.check_all_task()
        self.check_insert_task()
        self.check_update_task()
        self.check_delete_task()
        self.sync_scheduler_job_to_redis()
        end_time = time.time()
        print(f"总耗时：{end_time - start_time} seconds")


news_scheduler = NewsScheduler()
