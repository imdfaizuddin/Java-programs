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

print(check_prime())