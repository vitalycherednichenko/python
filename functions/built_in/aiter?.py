# Return an asynchronous iterator for an asynchronous iterable. Equivalent to calling x.__aiter__()

arr = [5, 6, 7, 8, 9]

async def sum(iterable, start=0):
    async for x in aiter(iterable):
        start += x

    return start

print(sum(arr))
