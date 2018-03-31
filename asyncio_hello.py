# -*- coding:UTF-8 -*-

import asyncio

@asyncio.coroutine # 将generator标记为coroutine类型
def hello():
    print("hello,world!") 
    r=yield from asyncio.sleep(1) # yield from异步调用async.sleep()函数[也是一个generator]
    print("hello,again!")

loop=asyncio.get_event_loop() # 搞到一个Eventloop

loop.run_until_complete(hello()) # 扔进去
loop.close() # 记得关掉
