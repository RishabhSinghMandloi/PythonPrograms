f = open("/home/admin1/myfile/abc.txt" ,'r')
#f.write("This is my file")
a=f.read().split(" ")
print(a)
f.close()

