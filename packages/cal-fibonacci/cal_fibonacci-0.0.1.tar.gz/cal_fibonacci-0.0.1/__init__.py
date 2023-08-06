def calculate_fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    a,b = 1,1
    for i in range(2,n):
        temp = a+b 
        a = b
        b = temp
    return temp


print(calculate_fibonacci(6))
