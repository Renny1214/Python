
#EXCEPTION HANDLING

#will throw exception because x is not defined
#if print(x) only writtten will gove an error
try:
  print(x)
except:
  print("An exception occurred") #will print this

#Print one message if the try block raises a NameError and another for other errors:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")  #will print this

#else will get printed if no error or exception occurs
try:
  print("Hello")      #will print this
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")      #will print this


#finnaly will get printed if error or exception occurs it doesnt care
try:
  print(x)
except:
  print("Something went wrong")     #will print this
finally:
  print("The 'try except' is finished")      #will print this

#erro in for loop
new_list =[1,2,3,'5',6,7]
#for item in new_list:
 #   item = item+50

empty_list_exceptions=[];

for item in new_list:
   try:
       item = item+50
       print(item)
   except Exception as e:
        print(e,"||",item)
        empty_list_exceptions.append(item)
        
print(empty_list_exceptions)


#raise an exception
x=-1;
if x<0:
   raise Exception("sorry , no number below 0")

#to define what kind of error to raise
x="heeloo"
if not type(x) is int:
   raise TypeError("only integers are allowed")


