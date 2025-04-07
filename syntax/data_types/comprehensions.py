squares = [x ** 2 for x in range(5)]

print(squares)

even_squares = [x ** 2 for x in range(5) if x % 2 == 0]

print(even_squares)

numbers_dict = {x: x ** 2 for x in range(5)}

print(numbers_dict)

unique_squares = {x ** 2 for x in range(-2, 3)}

print(unique_squares)

squares_gen = (x ** 2 for x in range(5))
print(next(squares_gen)) 
print(next(squares_gen))
print(list(squares_gen))
