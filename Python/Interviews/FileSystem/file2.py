'''Create and write file/ overrides if file already exists'''
# fw = open("test.txt","w")
# fw.write("Hello World 3")
# fw.close()
# fw.write("hi")  will give error after fw.close()

fr = open("test.txt","r")
data1 = fr.read()
# print(data1)

fa = open("test.txt", "a")
fa.write("\nkya baat hai")
fa.close()
fr = open("test.txt",'r')   #!'''need to open file again for reading the appended data'''
print(fr.read())