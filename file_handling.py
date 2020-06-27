#The key function for working with files in Python is the open() function.
#The open() function takes two parameters; filename, and mode.
#r-read a-append w-write x-create
#In addition you can specify if the file should be handled as binary or text mode
#t -text b-binary

f = open("abc.txt")
f = open("abc.txt","rt")   # here rt refers to read and text


#different modes and description
#r -read
#rb - reading only binary format
#r+ - read and write. The file pointer placed at the beginning of the file.
#rb+ - read and write in binary format
#w - writing only
#w+ - Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
#wb+  - Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing



f = open("abc.txt","r+")
print(f.read())

#specifynumber of charcters
f1 = open("abc.txt","r+")
str = f1.read(5)
print(str)

#to return one line
print(f.readline())

#loop
for x in f:
  print(x)

print("Name of the file: ", f.name)
print("Closed or not : ",f.closed)
print("Opening mode : ",f.mode)


#this adds the content at the end
f = open("abc.txt","a")
f.write("new content")
f = open("abc.txt","r")
print(f.read())

#this deletes the whole content overwrites it
f = open("abc.txt", "w")
f.write("Woops! I have deleted the content!")
f = open("abc.txt","r")
print(f.read())

#check current position(tell) and repostion it to the start(seek(0,))
f = open("abc.txt","r+")
str = f.read(10)
print(str)

position = f.tell()
print(position)

position = f.seek(0,0)
str  = f.read(10)
print(str)

#to rename a file
import os
os.rename("xyz.txt","xyz1.txt")

#to remove a file
os.remove("xyz1.txt")

#check if the file exists
if os.path.exists("xyz.txt"):
    print("file exists")
else:
  print("file does not exist")

#create a empty file
f2 = open("xyz.txt","x")

#file close
f.close()


