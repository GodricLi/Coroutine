import asyncio

"""
使用 async 定义了一个 execute() 方法，方法接收一个数字参数，方法执行之后会打印这个数字。随后我们直接调用了这个方法，
然而这个方法并没有执行，而是返回了一个 coroutine 协程对象。随后我们使用 get_event_loop() 方法创建了一个事件循环 loop，
并调用了 loop 对象的 run_until_complete() 方法将协程注册到事件循环 loop 中，然后启动。
最后我们才看到了 execute() 方法打印了输出结果。
可见，async 定义的方法就会变成一个无法直接执行的 coroutine 对象，必须将其注册到事件循环中才可以执行。
"""


async def execute(x):
    print('Number:', x)


coroutine = execute(1)
print('coroutine:', coroutine)
print('After calling execute')

loop = asyncio.get_event_loop()
loop.run_until_complete(coroutine)
print("After calling loop")


