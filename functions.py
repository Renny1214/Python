#declared a function print_name
def print_name(name):
    print("hello my name is {}".format(name))

print_name("renny")
print_name("mittal")


#*args for multiple argumaents
def add_numbers(*args):
    print(args)
    initial_sum=0
    for item in args:
        initial_sum += item
    print(initial_sum)

add_numbers(1,2,3,4)
add_numbers(4,5,6,7,8,9)

 
#**kwargs passes key value pairs and only one parameter is acceptable
def print_details(**kwargs):
    print("*************************************")
    print(kwargs)
    if 'name' in kwargs:
        print("hello {}".format(kwargs['name']))
    if 'address' in kwargs:
        print("Lives at {}".format(kwargs['address']))
    print("*************************************")


print_details(name="renny" , address ="#1490")
print_details(name="rashi")
