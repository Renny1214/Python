#tuples
#they are immutable therefore, we cant change the values already it has
t1=(1,23)
print(type(t1))

thistuple = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
print(thistuple)

#to access tuple items
print(thistuple[1])
#negative indexing means from the last
print(thistuple[-1])
#range of indexes
print(thistuple[2:5])  #in this 2 will be include and 5 not included
#range of negative indexes
print(thistuple[-4:-1])   #int this -4 included and -1 not included prints orange kiwi melon


#change tuple items (tuples are immutable therefore directly you cant change its value , converting it into list and back to tuple will do this for us)
y = list(thistuple)
y[1] = "hello"
thistuple = tuple(y)
print(thistuple)


#loop through a tuple
for x in thistuple:
    print(x)
      
#to check if tuple exists
if "apple" in thistuple:
    print("yes")
else:
    print("no")


#tuple length
print(len(thistuple))

#single element if added add , 
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #raise an error


#you cannot remove a single item in tuple but delete whole tuple
del thistuple
#print(thistuple)  #will give error

#join two tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 


    

import mysql.connector       
