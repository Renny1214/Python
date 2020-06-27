s1 =24;
print(s1)
print(type(s1))


s2 = 4.5;
print(type(s2))


var1= 25;
var2 =20;
print(type(var1))
print(var1+var2)
print(var1*var2)

print(abs(-40))

#print(dir(var1))

var3=23.899
print(round(var3,3))


s = '234'
print(type(s))
print(int(s))
print(type(int(s)))


l1 = [1,2,3,4,5,6];
print(l1)

#any kind of type can be inserted in list
l2 = [1,'renny',6,7.89,3,'mittal']
print(l2)

print(type(l2))

#to print one by one
for item in l2:
    print(item)


print(len(l2))

#to print with index
for index , item in enumerate(l2):
    print (index ,item)

#for single line print
for item in l2:
    print(item,end=" ")

#slicing of elements
l3 = l2[0:3]
print(l3)

#first element
print(l3[0])

#last element
print(l2[-1])

print(l2[:3])
print(l2[:-4])


#coverting string to list
str1 = 'renny'
#['r','e','n','n','y']
str2 = list(str1)
print(str2)


#adding value or appending
str2.append('m')
print(str2)

str2.insert(2,'i')
print(str2)

str2.pop(2)
print(str2)

str2[3] = 'h'
print(str2)


#list in list
str3=[1,2,3]
str2.append(str3)
print(str2)

str3 =[1,'renny' ,2,'mittal',3]

#for loop with if else
for item in str2 :
    if type(item)==str:
        print(item)
    if type(item)==list:
        for inner_item in item:
            print (inner_item)


#for loop and appending the new list
l5=['a','b','c',[1,2,3,4]]
temp_list=[]
for item in str2 :
    if type(item)==str:
        print(item)
        temp_list.append(item)
    if type(item)==list:
        for inner_item in item:
            print (inner_item)
            temp_list.append(item)


print(temp_list)

#to sort a list (only if the data is of same type)
#this doesnot effect the real list
print(sorted(l1))


#effect the real list
l1.sort()
print(l1)

#reverses the list
l1.reverse()
print(l1)

#prints min and max
print(min(l1))
print(max(l1))


#prints the third index value of the list
print(l2.index(3))

l6 =['r','e','n','n','y']
print(l6)

#joins the values return 'renny'
print(''.join(l6))
#returns r*e*n*n*y
print('*'.join(l6))

temp_list=[1,2,3,4,5,6]
#for loop from 0-5
for i in range(5):
    print(temp_list[i])


#for loop from 2nd to 5th index
for i in range(2,5):
    print(temp_list[i])


#for loop from 0 and have a differnce of 2
for i in range(0,len(temp_list),2):
    print(temp_list[i])


num1 =0; #false
num2= 1; #true
str1 ='' #false
str2='abc' #true
 
if True:
    print("yes")
if False:
    print("no")

if True:
    print("yes")
    print("helllo")
    print("yes")

if not num1:
    print("cant print")

if str1:
    print(str1)

n1= True
n2= False
if n1:
    print("n1")
else:
    print("n2")


#list
list_pattern =['abc','cd','ef','gh','hi']
for item in list_pattern:
    if 'abc' in item:
        print (item)
    else:
        print("abc not present in {}".format(item))

#squaring of list
l1 =[1,2,3,4,5]
l2=[];
for item in l1:
    l2.append(item*item)

print(l2)

#squaring of list in single line
l1 =[i*i for i in l1]
print(l1)


#find out even numbers in a list
l1=[1,2,3,4,5]
l2 =[]
for i in l1:
    if(i%2==0):
        l2.append(i)

print(l2)

#find out even numbers in a list in a single list
l2 = [i for i in l1 if i%2==0]
print(l2)
l2 = [i for i in l1 if i%2==0 if i>2]  #two conditions
print(l2)














