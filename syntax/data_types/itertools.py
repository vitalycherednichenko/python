from itertools import count

counter = count(10)  # Начинает с 10
print(next(counter))  # 10
print(next(counter))

from itertools import cycle

colors = cycle(["red", "green", "blue"])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))

from itertools import chain

combined = chain([1, 2], [3, 4], [5])
print(list(combined))
