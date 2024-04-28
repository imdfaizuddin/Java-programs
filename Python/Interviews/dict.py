# # freq = {}
# # a = "apple"
# # freq[a] = 2

# # print(freq)
# # print("apple" in freq)
# # print(a in freq)

# square = lambda x : x*x
# print(square(5))

# sum = lambda x, y, z : x + y
# print(sum(2,3,"x"))

x = 1
def demoFunc(x):
    x += 2
    print(x)
    def inside():
        print(x)
    inside()
demoFunc(x)
print(x)

name = "Faiz"
print(f"my name is {name}")