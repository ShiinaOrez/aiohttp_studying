import asyncio

@asyncio.coroutine # 修饰为coroutine
def wget(url):
    print("wget %s ..." % url) # 输出wget信息
    connect=asyncio.open_connection(url,80) # 建立连接
    reader,writer = yield from connect # 引入异步操作
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % url # 一行没什么用的代码
    writer.write(header.encode('utf-8'))
    yield from writer.drain() # 刷新底层传输的写缓冲区。也就是把需要发送出去的数据，从缓冲区发送出去
    while True:
        line=yield from reader.readline() # 读入一行header,事实上将writer.drain()注释掉也ok,因为readline中asyncio自动刷新了。
        if line == b'\r\n': # headers读完了
            break
        print ("%s header > %s" %(url,line.decode('utf-8').rstrip()))
    writer.close() # 关闭

loop=asyncio.get_event_loop()
tasks=wget('shiinaorez.github.io')
loop.run_until_complete(tasks)
loop.close()
