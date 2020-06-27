print ("hello")

s1 = "hello"
s1

s = len(s1)
print(s)

s2 = type(s1)
print(s2)

s3 = s1[0:2]
print(s3)

dir(s1)

s4 = s1.count('l')
print(s4)

s1 = s1.replace("hello","renny")
s1

print(s1)

s5 = 'renny\'s favourite fruit is pineapple'
print(s5)

s6 = "renny's favourite fruit is pineapple"
print(s6)


s7 = """
hello
my
name
is
renny"""
print(s7)

s1 = s1.lower()
print(s1)

s1 = s1.upper()
print(s1)

my_name = 'renny'
print("hello my name is %s"%my_name)

first_name='renny'
last_name='mittal'
work_at ='gemini'
print("hello %s %s. Working at %s"%(first_name,last_name,work_at))


first_name='renny'
last_name='mittal'
work_at ='gemini'
print("hello {} {}. Working at {}".format(first_name,last_name,work_at))
print("hello {0} {1}. Working at {2}. {0} {1}".format(first_name,last_name,work_at))

print("hello {first_name} {last_name}. Working at {work_at}".format(first_name=first_name,last_name=last_name,work_at=work_at))

