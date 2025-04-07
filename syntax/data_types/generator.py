def counter(n):
    i = 0
    while (i < n):
        yield i
        i += 1


for num in counter(5):
    print(num)
