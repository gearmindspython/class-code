# lists: ordered sequence of data 
# can contain mixed types of data 
# are mutable 

sample = [2, 'a', 4, [100, 200]]

print(len(sample)) # print out number of elements in list
print(sample[0])    
print(sample[0] + 1) # 0th element + 1 (2 + 1)
print(sample[3])    # prints 3rd element
print(sample[3][0]) # prints 0th element of 3rd element

# mutable lists
sample[0] = 5 
print(sample)

# iterating over a list
for elements in sample:
    print(elements) # prints each element on a new line
    
# appending to a list, adds to end of list
sample.append('hello')
print(sample)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

# removing elements, specify value to remove
list3.remove(5)
print(list3)

del(list3[1])   # del(list_name[index]) will be removed
print(list3)

list3.pop()     # .pop() remove the last element in the list 
print(list3)

# converting lists to strings and vice versa
message = 'i <3 cs'
message_to_list = list(message) # create a list with each character in message

#list(string_variable) - return a list with every character from string_variable
print(message_to_list)

# .join(listName) converts list to string
list_to_string = ''.join(message_to_list)
print(list_to_string)

# .sort(), reverse
blob = [509, 35, 124, 0, 956, 293948572, 7]
blob.sort() # sort the list into ascending order 
print(blob)

blob.sort(reverse = True)
print(blob)

# tuples 
# ordered sequence of elements, multiple types 
numTuple = (1, 2, 3)
# also define tuples without the ()'s numTuple = 1, 2, 3
# tuples are immutable, whereas lists are 
# recommend tuple usage if you just want to iterate over 
print(numTuple, type(numTuple))

# can print these out like lists
print(numTuple[0])

# you cannot modify a tuple
# numTuple[1] = 0  - you will get an error 
# you also cannot do .append(), .remove(), .pop() 

# converting lists to tuples, vice versa 
randomList = [3, 'orange', 39]
print(tuple(randomList))    # tuple(listName) to convert list -> tuple

randomTuple = ('apple', 'water', 3289589235)
print(list(randomTuple))  # list(tupleName) to convert tuple -> list

# list of tuples to print stuff out 
report = [("Aviral", 4.0), ("Ronak", 4.0), ("Kate", 4.0), ("Aadi", 4.0)]
for student in report:
    for gpa in student:
        print(gpa)
        
# tuple of tuples
tuplesSquared = (('x', 'y', 'z'), ('X', 'Y', 'Z'))
print("This is a tuple of tuples: " + str(tuplesSquared))

# "modifying" a tuple 
anotherTuple = (34, 'a', 42374832, [88, 99])

print("This is our tuple before modifying: " + str(anotherTuple))
# we can change the value of mutable elements in a tuple
# in this case, our list is mutable
# tupleName[indexOfListInTuple][indexToModify]
anotherTuple[3][0] = 723883 
anotherTuple[3][1] = 'almond'

print("This is our tuple after modifying: " + str(anotherTuple))

# dictionaries 
# key : value 
# dictionaries do not have an order 
# dictionaries must have a key and value, where lists jsut have values

# define a blank dictionary
blank_dictionary = {}

# define a dictionary with numeric keys
num_dictionary = {1: 'soccer', 
                  2: 'baseball'}

# dictionaries support mixing data types
mix_dictionary = {'class': 'python', 
                  'students' : [0, 1, 2, 3]}
print(mix_dictionary)

# iterating through dictionary 
directory = {'Student Name' : 'Berry', 
             'Subject': 'Biology',
             'Classroom': 321}
# for loop to print out keys
for keys in directory:
    print(keys)
    
# printing out keys and values
print("{Keys}:{Values}")
for keys, value in directory.items():
    print(str(keys) +  ": " +  str(value))

# add to dictionary 
# dictionaryName[Key] = Value
directory['Hallway'] = 'J'
print(directory)

# removing from dictionary 
# dictionaryName.pop(Key) # parameter is optional 
directory.pop('Hallway')
print(directory)

# removes a random element
directory.popitem()
print(directory)

# deleting all items from dictionary
# directoryName.clear()
directory.clear()
print(directory)

# eliminting the dictionary object 
# del dictionaryName
del directory
# print(directory) - error, directory is deleted at this point