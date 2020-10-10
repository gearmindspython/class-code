# files 
# file: named location on system storage that holds data for access

# steps for file processing
# 1: open file 
# 2: read or write from/to file 
# 3: close file 

# opening a file 
# file_object = open(file_name, access_mode, buffering)
# file_object = reference to file_name
# file_name = name of the file we want to use 
# access_mode = represents the way we want to open the file (optional)
# buffering - the way your computer communicates with file 

# opening a file for reading
# inputFile = open("input.txt", 'r') - opens 'input.txt' 

# opening a file for writing
# outputFile = open("output.txt", 'w') - opens 'output.txt' 

# opening a file for appending
# appendFile = open("output.txt", 'a') - opens 'output.txt' 4 appending

# close the file
# file_object.close()

# reading a file: methods
# 1 - for loop 
# 2 - .read() - read the entire contents of the file as a string
# 3 - .readline() - reads a single line
# 4 - .readlines() - read the entire contents of the file, each line of the file is a string, putting that string in a list

# writing to a file
outputFile = open("output.txt", 'w')

# one way of writing to file
print("Hello World!", file=outputFile)


# another way of writing to file 
outputFile.write("this is another message I am writing")

# file encoding, writing to file
with open('app.log', mode = 'w', encoding = 'utf-8') as fileObject:
    # write first line
    fileObject.write("This is my first file, first line!\n")
    
    # write second line
    fileObject.write("This is line two.\n")
    
    # write third line
    fileObject.write("This is the third line.\n")
    
# reading from file
with open('app.log', 'r', encoding = 'utf-8') as fileObject:
    # content is the list created from readlines() method
    content = fileObject.readlines()

# for loop to print content
for line in content:
    print(line)
    

# example: reading from a file
listOfLines = ['Python', 'Java', 'PHP', 'HTML', 'JavaScript', 'AngularJB']

# create our file 
def createFile():
    langFile = open("languages.txt", 'w')
    
    # add list elements to file
    for line in listOfLines:
        langFile.write(line)
        langFile.write("\n")
        
    # !!!!!!!!! don't forget to close your file
    langFile.close()
    
# read our file 
def readFile():
    readLang = open('languages.txt', 'r')
    
    # reading list of lines
    output = readLang.readlines()
    # readline reads until the newline character is met '\n'
    
    readLang.close()
    return output 

# main function
def main():
    
    # create languages.txt
    createFile()
    
    # read lines from languages.txt
    # outputList is the list created becasue of readline method in readFile
    outputList = readFile()
    
    # iterate over list 
    for lines in outputList:
        print(lines)

main()

# error/exceptions/handling 
# error: when something goes wrong 
# errors occur at compile time 

# exception: it occurs during execution, disrupts program 
# quotient = 1 / 0

# try/except statement 
# try block: code that can raise an exception 
# except block: code that handles an exception 

try: 
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    quotient = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")

# else will execute when there are no exceptions
else:
    print("Legit divison")
    print(quotient)

# try/except/finally 
# try: code that can raise an exception
# except: code that handles exception
# finally: code that will always execute 
try:
    print("Hello!")
    quotient = 5/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This is going to be executed all the time.")