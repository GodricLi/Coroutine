import asyncio
import requests

"""
为某个 task 绑定一个回调方法
"""


async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status


def callback(task):
    print('Status:', task.result())


coroutine = request()
task = asyncio.ensure_future(coroutine)
task.add_done_callback(callback)            # 给task绑定一个回调方法，或者直接使用task.result()
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('Task callback:', task.result())