#Solution 1: Time Complexity O(2^n), Space Complexity O(n)
# def fibonacci(n):
#     if n == 0: return 0
#     if n == 1: return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

#Solution 2: Time Complexity O(n), Space Complexity O(n)
# def fibonacci(n, fib = {0: 0, 1: 1}):
    
#     if n in fib: return fib[n]
#     else:
#         fib[n] = fibonacci(n - 1, fib) + fibonacci(n - 2, fib)
#     return fib[n]


#Solution 3: Time Complexity O(n), Space Complexity O(1)
def fibonacci(n):
    first = 0
    second = 1
    if n == 0: return 0
    if n == 1 or n == 2: return 1
    for _ in range(n):
        first, second = second, first + second
    return first

print(fibonacci(8))