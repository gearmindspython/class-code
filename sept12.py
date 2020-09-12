# conditionals
# if statement - executes when condition is true
# if <condition>:
#   <expression>
# else: - executes when if is False 
#   <expression>

# if/elif/else - if, else if, else
# if <condition>:
#     <expression>
# elif <condition>:
#     <expression>
# else:
#     <expression> 

# ask the user if they are hungry
hungry = input("Are you hungry? ")

# if yes, print 'go to the grocery store' 
if hungry.lower() == 'yes':
    print("Go to the grocery store!")
    
    # cost of chocolate bar
    cost = float(input("What is the price of a chocolate bar? $"))
    
    if cost < 1.00:
        print("Buy 3 chocolate bars")
    else:
        print("You can only afford 1.")
    
# else, we just print not hungry
else:
    print("You are not hungry.")
 
# ask if want to play video game   
game = input("Do you want to play a video game? ")

# if yes, print glhf
if game.title() == 'Yes':
    print("GLHF. Don't ragequit!")
elif game.title() == 'No':
    print("Go watch TV, take a nap, or do your homework.")
else:
    print("I don't understand.")
    
# comparison operators 
# if var1 > var2 - if var1 is greater than var2
# if var1 >= var2 - if var1 is greater than or equal to var2
# if var1 < var2 - if var1 is less than var2
# if var1 <= var2 - is var1 is less than or equal to var2
# if var1 == var2 - if var1 is the same value as var2 
# if var1 != var2 - if var1 is not equal to 

# logical operators (only work on booleans)
# not, and, or - 3 main oeprators
# status = True
# playing = True
# if not status - if status is False
# if status and playing - if status and playing are True
# if status or playing - if either status or playing is True

# while loops
# stepper_variable = 0
# while <condition>:
#   <execution body>
#   stepper_variable += 1
# in a while loop, it will repeat until <condition> is False

counter = 0
name = input("Enter your name: ")
while counter < 10:
    print("Hello " + name + "!")
    print("We are on iteration number " + str(counter))
    counter += 1
print("End")

total = 0
number = int(input("Enter a number: (Enter 0 to end the program)"))
while number != 0:
    total += number
    print("The total is now: " + str(total))
    number = int(input("Enter a number: (Enter 0 to end the program)"))
print("The final total is :")

# for loop 
mySum = 0
for counter in range(7, 10):
    mySum += counter 
print(mySum)

mySum = 0
for counter in range(5, 11, 2):
    mySum += counter
    
    if mySum == 5:
        break
print(mySum)

# printing out numbers
n = 0 
while n < 5:
    print(n)
    n += 1

for n in range(5):
    print(n)

# for loops
# know the number of iterations 
# uses a counter
# can rewrite for loops using a while loop

# while loops
# unknown number of iterations 
# can use a counter, but must initialize before loop
# requires increment of counter variable 
# may not be able to rewrite while loops as for loop

 menu 
done = False 
while not done: 
    print("Welcome to the menu!")
    print("I - Introductory Problem")
    print("E - Print even numbers")
    print("Q - Quit")
    
    option = input("Enter an option: ")
    if option.upper() == "I":
        print("We are doing the introductory problem.")
        
        counter = 0
        name = input("What is your name? ")
        
        while counter < 5:
            print(name)
            counter += 1
    
    elif option.upper() == 'E':
        print("We will be printing even numbers between 2-10")
        
        for even in range(2, 11, 2):
            print(even)
    
    elif option.upper() == 'Q':
        print("We are now exiting.")
        print("Have a good day!")
        done = True
    
    else:
        print("I don't understand.")