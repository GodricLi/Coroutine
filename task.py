import asyncio


"""
task，它是对 coroutine 对象的进一步封装，它里面相比 coroutine 对象多了运行状态，
比如 running、finished 等，我们可以用这些状态来获取协程对象的执行情况。
在上面的例子中，当我们将 coroutine 对象传递给 run_until_complete() 方法的时候，
实际上它进行了一个操作就是将 coroutine 封装成了 task 对象，我们也可以显式地进行声明
"""


async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling excute')

# 直接通过 asyncio 的 ensure_future() 方法，返回结果也是 task 对象
# task = asyncio.ensure_future()
loop = asyncio.get_event_loop()
task = loop.create_task(coroutine)
print('Task:', task)
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')
