#Section 5

#Functions
#Example
def convert(amount):    # times any number by 1.75
    output = amount * 1.75 
    return output
 
print(convert(10)) # whatever value is inside the print statement takes place of 'amount'

#Example
def yer(foo):          # times any number by itself
    itself = foo * foo 
    return itself
    
print(yer(3)) 



#Conditionals
x = 1
y = 1

#Example
if x == 1 and y==1:
    print("Yes")
else:
    print("No")

#Example: Define a function that: takes a string as a parameter, returns False if the
#                                 string contains less than 8 characters or
#                                 returns True if the string contains 8 or more characters
def foo(str):
    if len(str) < 8:
        return False
    else:
        return True
    
print(foo("yea"))

#Example
x = float(input("Say Sum: ")) #use float bc it's more versatile than int
y = 5

if  x > y:
    print("x is greater than y fr")
elif x == y:
    print("x is equal to y fr")
else:
    print("x is less than y fr")

#Example

def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))



