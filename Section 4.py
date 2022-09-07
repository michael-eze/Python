#Section 4

#Lists
#Example
temperatures = [9.1, 8.8, 7.5]
temperatures.append(4.1) #all methods end with () , with object inside 
print(temperatures)

#Example
seconds = [1.23, 1.45, 1.02]
current = 1.11
seconds.append(current)
print(seconds)

#Example
temperatures.clear() #clears all items in list
print(temperatures)



#Indexing
#Example
temperaturess = [9.1, 8.9, 7.5]
index = temperaturess.index(7.5) #gives index of item in list
print(index)

#Example
secondss = [5.43, 2.25, 1.12, 17.38, 16.00, 4.44]
#secondss.remove(4.44) #removes item in list
print(secondss)
print(len(secondss)) #shows length of lists
print(secondss[1:4]) #shows items from index 1 - 3
print(secondss[-1]) #shows last item fromt the back
print(secondss[-3:-1]) #shows list from 3rd to last - 1st to last



#String Indexing
#Example
string = 'yafeme'
print(string[1])
print(string[-3])

#Example
stringy = ['yafeme', 1, 2, 3]
stringy[0][2] #chain indexing, does first item and then second item in that 1st



#Dictionary Indexing
Dict = {"Karr": "Kenn", "KkParty": "Khen", "Tyren": "Zach"}
print(Dict["KkParty"])


