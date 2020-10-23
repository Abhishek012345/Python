# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:05:16 2019

@author: Mukesh
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:04:20 2019

@author: Mukesh
"""
# CONDITIONAL STATEMENTS
######################## If condition ########################################
#one condition
a = 330
b = 200
if b > a:
  print("b is greater than a")
  
  
################# If else condition #######################################
#  two conditional statements
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#######################  If elif else condition ##########################
#  3 conditional statements
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
  
  
  # 5 if conditional statements
name = 'excelr'
if name == 'Fred':
     print('Hello Fred')
elif name == 'Xander':
     print('Hello Xander')
elif name == 'Joe':
     print('Hello Joe')
elif name == 'Arnold':
     print('Hello Arnold')
else:
     print("I don't know who you are!")
     
     
     
########################### nested if condition ##############################
x = 9


if x>10:
    print("ten")
    if x>20:
        print("yes")
    else:
        print("no")
        






if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")




############# Loops #####################
                
# for Loop
    
#For loop allows code to be executed repeatedly or iterations

#Ex:1
    
fruits = ["apple", "banana", "cherry"]


print("apple")


for x in fruits:
  print(x)          #looping stops when it reach the last item or element

  

for x in range(len(df):          #0,1,2,3,4,5 - 6
  print(x)
else:
  print("Finally finished!")



## finding square of values by using a forloop
numbers = [1, 2, 4, 6, 11, 20]
# iterating over the given list
for abc in numbers:

    # calculating square of each number
    sq = abc * abc * abc
    # displaying the squares
    print(sq)

    
############# Nested for loop ####################
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)      #combinations
   


for num1 in range(3):         #0,1,2    
	for num2 in range(10, 14):    #10,11,12,13 
		print(num1,",",num2)

###############################################################################
# While Loop
# while loop will run the code repeatedly only when the given condition is true:

count = 25

while count <= 20:
    print("Digit: ", count)
    count = count + 1

print("Thank you")     #repeteadly coding will be done





import random   #(numpy) # random package helps me to get random numbers 

n = 20

random_number = int(20 * random.random())

guess = 0

while guess != random_number:
    guess = int(input("put New Number: "))
    if guess > 0:                        
        if guess > random_number:
            print("number is too large")
        elif guess < random_number:
            print("number is too small")     
    else:
        print("sorry that you are giveup!")
        break
else:
    print("Congratulations. YOU WON!")



    
    
################################################################################
    
# user defined functions   # named functions

def add_numbers(x,y):
   sum = x + y
   return sum



def avg_number(x, y):
    print("Average of ",x," and ",y, " is ",(x+y)/2)
    
avg_number(3, 4)



## Define a function with conditional statement
    
def max_num(num1,num2,num3):
    
    if num1 >= num2 and num1 >= num3:
        
        return num1
    
    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3
    
print (max_num(400,60,1150))




def evenOdd( x ): 
    if (x % 2 == 0): 
        print ("even")
    else: 
        print ("odd")


evenOdd(2) 
evenOdd(3)


############### Lambda expressions ########################################

def cube(y):                      #user define function
    return y*y*y; 
  
 # lambda functions are anonymous expression i.e (function without any name)

g = lambda x: x*x*x 
print(g(7)) 

  

#filter function will filter the elements or items that satisfies the condition

list1 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list1 = list(filter(lambda x: (x%2 != 0) , list1)) 
print(final_list)


# map function will helps to apply the condition to all elements one by one

list2 = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list2 = list(map(lambda x: x*2 , list2)) 
print(final_list) 
