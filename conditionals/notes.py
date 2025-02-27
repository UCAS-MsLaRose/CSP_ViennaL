#Vienna LaRose, Condtionals notes Python
name = input("What is your name?:\n")
#1. What puts something inside of the “if” statement?
if name == "LaRose":
    print("Hi Ms. LaRose")
else: #This happens if the condition is false
    print(f"Hello {name}!")

#2. What do if statements do?
    #Checks a condition and if it is true it wll do a thing
if name == "LaRose": # <= this is the condition
    print("Hi Ms. LaRose") #<=This is what it does if true

#3. What are boolean statements? 
if name == "LaRose": # <= This is the boolean statement. It is either true or false
    print("Hi Ms. LaRose")
else: 
    print(f"Hello {name}!")

#4. What do else statements do?
if name == "LaRose": 
    print("Hi Ms. LaRose")
else: #if the boolean is false, the else statement happens
    print(f"Hello {name}!")

#5. What kind of statement do you use if you have more than 2 needed outcomes?
num = int(input("How many cookies are there:\n"))
#computers read top to bottom, check the least likely first
if num == 0: #<= if always starts the conditional
    print("There are none.")
elif num == 1: #everything inbetween should be elif
    print("There is one.")
elif num <4:
    print("There are a couple")
elif num < 10:
    print("There are a few")
else: #<= else always ends the conditional
    print("There are many")

#6. What do each of the different symbols mean in conditionals? 
# < Less than
# > Greater than
# <= Less than or equal to
# >= Greater than or equal to
# == Equal to
# === *Dosen't exsist in python 
# ! Not

#7. What are the 3 logical operators?
if num <10 and num > 5: #And means both booleans must be true
    print("This is a big single digit number")

elif num <10 or num > 5: #or means one must be true
    print("This is a single digit number")

elif not num < 10: #Not changes to check if false
    print("This is a not single digit number")

#8. What are logical operators for?
    #Allows the code to handle more difficult questions. . .increases complexity

#9. What does a nested conditional statement do?
if num <10:
    if num ==8:
        print("This prints at 8")
    else:
        if num == 4:
            print("There are only enough cookies left for me. . . sorry")
        else:
            print("The number is less than 10")
else:
    print("The number is bigger than 10")
