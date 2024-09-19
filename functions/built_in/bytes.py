# Return a new “bytes” object which is an immutable sequence of integers in the range 0 <= x < 256
# The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified,
# and bytearray() returns an object that can be modified.

x = bytes(10)

print(x)