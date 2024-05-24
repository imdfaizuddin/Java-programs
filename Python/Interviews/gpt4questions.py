'''Check Prime'''
def check_prime():
    n = 89343745911121
    # n = 28238519
    if n <=1:
        return False
    for i in range(2,int(n**0.5)+1):    #n ** 0.5 == math.sqrt(n)
        if n % i == 0:
            return False
    return True


# print(check_prime())

'''Fibonacci sequence'''

def fibo():
    n = 10
    ans = [0,1]
    fib = 0
    if n == 1:
        return ans[0]
    if n == 2:
        return [0]
    first = 0
    second = 1
    i = 3
    while i <= n:
        fib = first + second
        ans.append(fib)
        first = second
        second = fib
        i+=1
    return fib,ans
    
print(fibo())