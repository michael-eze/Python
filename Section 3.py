#Section 3

x = 10 #int
y = '10' #string
z = 10.1 #float

sum1 = x + z
sum2 = y + y

print(sum1,sum2)
print(type(x), type(y), type(z)) #shows type of class you using



#Lists [], uses brackets
grade = [9.1, 8.8, 7.5]
print(max(grade))

#Example: How many times does 10.0 show in this list?
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print("It shows", student_grades.count(10.0), "times")



#Range
grades = [9.1, 8.8, 7.5]
print(grades*3)
 
gradess = list(range(0, 15, 2)) #goes 0 - 15 in increments of 2
print(gradess)



#Directory
dir(int) #shows methods of what class you are usings
dir(__builtins__) #shows built-in methods of pythons
print(dir(int))
help(int.real)
                


#Dictionary {}, use curly brackets, use keys and values
temperatures = {"Mon": 91, "Tue": 88, "Wed": 75} #goes keys: values
print(temperatures.keys())
print(temperatures.values())
print(max(temperatures.values()))

 

#Tuples (), uses parenthesis instead of brackets
student_grades = (9.1, 8.8, 7.5)
print(student_grades)
