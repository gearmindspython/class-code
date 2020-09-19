# Greatest Common Denominator/Divisor (GCD) function
# calculates the GCD between two numbers
def GCD(num1, num2):
    minimum = num2 if num1 > num2 else num1
    factor = 1
    
    for icount in range(1, minimum + 1):
        if num1 % icount == 0 and num2 % icount == 0:
            factor = icount

    return factor

# get_int allows user to input a number
def get_int():
    return int(input("Enter a number: "))

# main function references the other two
def main():
    num1 = get_int()
    num2 = get_int()
    
    print(GCD(num1, num2))

# only need to reference main, since it will refernce the other two 
main() 

# variable scope - where your variable lives 
# two different types: global and local 
# global - access it anywhere
# local - only be defined in a function, only accessible inside of a function 

x = 25 

def main():
    x = 10
    print(x)

# program actually starts here
main()  # calling main, x = 10 inside main
print(x)   # outside main, x = 25 here 

# another scope example
def g(x):
    def h():
        x = 'abc'
        print("Inside of H, x =", x)
    x = x + 1
    print("Inside of G, x =", x)
    h()
    return x

x = 3
z = g(x) 
print("Outside of G and H, x =", x)

# program template 
# declare and initialize any global variables 
# .
# .
# function defintions
# def funct1():
#   funct1 body
# .
# .
# def funct2():
#   funct2 body
# .
# .
# main function
# def main():
#   main body
#   main calls above functions to accomplish tasks
# this is the template we will be using to write a program

# strings
# methods .lower(), .upper(), .title() 
name = 'Kate'
print(len(name))

#  strings
# methods .lower(), .upper(), .title() 
name = 'Kate'
print(len(name))    # len() returns length of string

# indexing 
print(name[0])  # returns 'K' - 0 is the index for first character
print(name[1])
print(name[2])
print(name[3])
# print(name[5])  # error, out of bounds
print(name[-1]) # returns 'e', -1 is the first element backwards 
print(name[-2])
print(name[-3])
print(name[-4])

# slicing/indexing 
blob = 'abcdefgh'
print(blob[3:6])    # starts at index 3, ends at 5 (1 - last parameter)

# slicing/indexing 
blob = 'abcdefgh'
print(blob[3:6])    # starts at index 3, ends at 5 (1 - last parameter)
print(blob[3:6:2])  # starts at index 3, ends at 5, increments in 2
print(blob[::]) # prints the whole string 
print(blob[::-1])   # print the whole string backwards
print(blob[4:1:-2]) # starts at index 4, to index 1, increments backwards by 2 (negative)

# strings are immutable - can't modify it
name[0] = 'y'   # gives us an error, can't modify


blob = 'abcdefgh'

# iterating through a string with for loop
for character in range(len(blob)):
    if blob[character] == 'a' or blob[character] == 'b':
        print("There is an a or b in blob")

# 'traditional' 
for character in blob:
    if character == 'a' or character == 'b':
        print("There is an a or b in blob")

# example 3
# function that accepts a string
# calculates the number of upper & lower case letters
def calculate(phrase):
    numLower = 0
    numUpper = 0
    
    for character in phrase:
        if character.isupper():
            numUpper += 1
        elif character.islower():
            numLower += 1
        else:
            pass
    
    print("Number of lower case letters:", numLower)
    print("Number of upper-case letters:", numUpper)

calculate("The quick Brow Fox")
