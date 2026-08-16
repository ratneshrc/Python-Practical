#read
file = open("example.txt", "r")
data = file.read()
print(data)
file.close()


#write
file = open("example.txt", "w")
file.write("Hello Python\n")
file.write("Learning File Handling")
file.close()


#append
file = open("example.txt", "a")
file.write("\nThis is new data.")
file.close()




#create
try:
    file = open("newfile.txt", "x")
    file.write("This is a new file.")
    file.close()
except FileExistsError:
    print("File already exists.")
    
    
    
#read + write
file = open("example.txt", "r+")
data = file.read()
print(data)
file.write("\nNew data")
file.close()



#write + read
file = open("example.txt", "w+")
file.write("Hello Python")
file.seek(0)
data = file.read()
print(data)
file.close()



#append + read
file = open("example.txt", "a+")
file.write("\nNew data added")
file.seek(0)
data = file.read()
print(data)
file.close()



#read-binary
file = open("image.jpg", "rb")
data = file.read()
print(data)
file.close()




#write-binary
file = open("copy.jpg", "wb")
file.write(data)
file.close()



#append-binary
file = open("data.bin", "ab")
file.write(b"Hello")
file.close()