# Write a function 'fib(n)' that takes in a number as an argument.
# The function should return the n-th number of the Fibonacci sequence.

# The first and second number of the sequence is 1.
# To generate the next number of the sequence, we sum the previous two.

# def fib(n):
#     if n <= 2:
#         return 1
#     return fib(n - 1) + fib(n -2)
# '''''''
# print(fib(6))
# print(fib(50))

# if our argument is too big, it can cause issues, we need to further =>
# improve our algorithm

# memoization
# reminder, capturing data to use later
# object for JS, dictionary for Python
# keys will be arg, value will be return value

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    return fib(n -1) + fib(n - 2)

print(fib(6))
print(fib(20))
# print(fib(50))