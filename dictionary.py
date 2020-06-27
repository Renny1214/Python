
#dictionary work as map
#it cannot have list as key
#it doesnt allow any mutable type to be the key
#not ordered structures
d1 = {'key1':'value1',1:2} 
print(d1)
print(type(d1))


#To print the value of particular key
x = d1[1]
print(x)

x = d1.get("key1")
print(x)


#To change the value of a key
d1["key1"] = "xyz"

#just returns the keys & looping through a dictionary
for item in d1:
    print(item)

#just returns the values
for item in d1:
    print(d1[item])
       #or
for item in d1.values():
    print(item)
    
#to return both keys and values
for x,y in d1.items():
    print(x,y)

#check if key exists
if "key1" in d1:
    print("yes")

#dictionary length
print(len(d1))


#adding item
d1["key2"] = "value2"
print(d1)

#removing items
d1.pop("key1")
print(d1)

#to completely del the whole dictionary
#del d1
    #print(d1) -will give error

d2= {'key1':'value1',1:2}
#to clear method empties the dictionary
d2.clear()
print(d2)

#del keyword removes the item with the specific key name
del d1["key2"]
print(d1)

#to copy a dictionary
d3 = d2.copy()
print(d3)
    #or
d4 = dict(d2)
print(d4)


#nested dictionary
d5 = {
    "a":{"name":"renny",
         "age":21},
    "b":{"name":"abc",
         "age":20}
    }

print(d5)

#if you want dictionaries that already exists as dictionaries
a = {"name":"renny",
         "age":21}
b = {"name":"abc",
         "age":20}

family={"child1" : a,
        "child2" : b}

print(family)

#iteritem is removed from python 3
for key1,value1 in family.items():
    print("key:",key1)
    print("value:",value1)

#in same order using assign
assign = d1.keys()
print(assign)
for item in assign:
    print(d1[item])

d1['new_key'] = 'new_value_added'
d1
d1[1] = 'override_key'
d1
