# lists/dictionaries/tuples exercises 

# problem 1
# create a list named sales,
# use a loop to enter sales for 7 days
# print total amount of sales
sales = [] 

# get the sales for 7 days
for days in range(7):
    todaysSales = float(input("How much were the sales today? $"))
    sales.append(todaysSales)
 
# iterate over list to get total    
total = 0
for salesIndex in sales:
    total += salesIndex

# print total 
print("Total Sales: $" + str(total))

# problem 2
# create a list of 10 positive & negative numbers
# print number of positive numbers
# print number of negative numbers
# print number of 0's 
listOfNums = [95, 80, 90, 99, 75, -2, -100, -50, -40, -30]

numPositive = 0
numNegative = 0
numZeroes = 0 

# iterate over list to calculate
for value in listOfNums:
    if value < 0:
        numNegative += 1
    elif value > 0:
        numPositive += 1
    else:
        numZeroes += 1

# print results 
print("Number of Positive Numbers: " + str(numPositive))
print("Number of Negative Numbers: " + str(numNegative))
print("Number of Zeroes: " + str(numZeroes))

# problem 3
# printing average of positive #'s
# printing average of negative #'s
sumPositive = 0.0
sumNegative = 0.0

# iterate over list to get sums
for value in listOfNums:
    if value < 0.0:
        sumNegative += value
    elif value > 0.0:
        sumPositive += value
    else:
        continue 

# get average 
avgPositive = sumPositive / numPositive
avgNegative = sumNegative / numNegative

# print results 
print("Average of Positive Numbers: " + str(float(avgPositive)))
print("Average of Negative Numbers: " + str(float(avgNegative)))

# tuples (), immutable 
# immutable - cannot modify at all 
exampleTuple = (456, 'ads', 'Hello', [59, 482, 485], (3285, 4238))
# listName[index] = sajidfjas

print("Tuple before 'modifying'" + str(exampleTuple))
# cannot change the value of any tuple's elements 
# you can modify a tuple if tuple's data type is Mutable
exampleTuple[3][0] = 'whatever value'

print("Tuple after 'modifying'" + str(exampleTuple))

# dictionaries - key : value

# activity with dictionaries
done = False
friends = {"Sofia" : "Peterson", "Hannah" : "Dallas", "Bernadette" : "Richardson"}

while not done: 
    print("Welcome to the friend example!")
    print("S - Show friends and their cities")
    print("A - Add a friend and their city")
    print("D - Deleting a friend")
    print("Q - Quit")
    
    choice = input("Enter an option: ")
    
    # show key and values in dictionary
    if choice.upper() == 'S':
        print("This option will list our friends and the city they live in.")
        for key in friends:
            print(key, "\t", friends[key])
    
    # add to dictionary
    elif choice.upper() == 'A':
        # dictionaryName[key] = value
        friends["Gillian"] = "Fort Worth"
        
    # deleting specific friend from dictionary 
    elif choice.upper() == 'D':
        # dictionaryName.pop(key)
        friends.pop("Hannah")
    
    # quit
    elif choice.upper() == 'Q':
        print("Have a good day!")
        done = True
    
    # error checking
    else:
        print("I do not understand.")
            
