
# Fibonacci series using recursion
def fibonacci(n):
    if n ==0 or n==1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
 
 
a=int(input("Enter the number:\n"))
ans=fibonacci(a)
print(ans)