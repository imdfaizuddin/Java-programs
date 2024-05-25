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
    
# print(fibo())

'''Sum of Digits of a Number'''
def sum_of_digits():
    n = 41515
    s = str(n)
    sum = 0
    for i in s:
        i = int(i)
        sum += i
        
    print(sum)
    sum2 = 0
    temp = n
    rev = 0
    while temp:
        r = temp % 10
        rev = rev*10 + r
        sum2 += r
        temp = temp//10
        
    print(sum2, rev)

sum_of_digits()