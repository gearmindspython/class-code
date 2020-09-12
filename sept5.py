# prints my name
print("Kate")
print("Making sure this works")
print(1234567890)

# data types 
# int - positive or negative whole numbers 
months_in_year = 12
days_in_year = 365
year = 2020

# float - decimal numbers
coffee = 1.99
tuition = 5002.20 
avocado = .46 

# string - characters 
name = 'Kate'
age = 21
friend = "Sophia"
university = 'UTD'

# boolean - True or False
hot = True 
summer = False 

# output 
print("Hello World!")
print('Hello world again from single quotes 8)')
print(23)
print(coffee)
print(university)

# string concatenation
first = 'Kate'
last = 'Malinis'
print(first + ' ' +  last)

# string methods 
first.lower()  # makes all characters lowercase
first.upper()   # makes all characters uppercase
first.title()   # capitalizes the first letter

# string formatting
print("Hello! My name is " + name + "and I am " + str(age))
print("Hello my name is %s and I am %d years old." %(name, age))

# escape sequences 
print("This is one line. \n This is another line")  # \n = newline, enter to new line

# input 
numberOfMovies = int(input("How many movies have you seen this summer?"))
print(numberOfMovies)

born = int(input("What year were you born? "))
year = int(input("What is the current year? "))
current_age = year - born
print("You are " + str(current_age) + " years old!")