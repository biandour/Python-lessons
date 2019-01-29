#! -*-coding:utf8-*-

import asyncio
from asyncio.futures import Future
import time


# async def hello(name):
#     await asyncio.sleep(2)
#     print('hello, ', name)
#
#
# coroutine = hello('world')  # async关键字定义的函数是一个coroutine，返回coroutine对象
#
# task = asyncio.ensure_future(coroutine)  # 将coroutine转为task对象
#
# print(isinstance(task, Future))  # True  task是Future的实例

'''
取得返回值和绑定回调函数的方法
'''
# async def _sleep(sec):
#     time.sleep(sec)
#     return '暂停了{}秒'.format(sec)
#
# coroutine = _sleep(2)
# loop = asyncio.get_event_loop()
#
# task = asyncio.ensure_future(coroutine)
# loop.run_until_complete(task)
#
# # task.result() 可以取得返回结果
# print('返回结果：{}'.format(task.result()))


async def _sleep(sec):
    time.sleep(sec)
    return '暂停了{}秒'.format(sec)


def callback(future):
    print('这是回调函数，获取的结果是：', future.result())


coroutine = _sleep(2)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(coroutine)

# 添加回调函数
task.add_done_callback(callback)

loop.run_until_complete(task)


