print(ord("A")) #output 65
print(ord("Z")) #output 90
print(ord("a")) #output 97
print(ord("z")) #output 122

print("Hello", "end", 87, True, end="\n") #end="\n" == print in nextline
print("next line")

x = 10
y = 3
print(x//y) #returns the 'integer' or 'floor' value quotient

hello = "heLLo World"
print(hello.upper())    #HELLO WORLD
print(hello.lower())    #hello world
print(hello.capitalize())   #Hello world
print(hello.count("l")) # 1 counts the number of 'l'
print(hello.lower().count("l")) # 3 converts the string into lowercase then counts the no. of "l"