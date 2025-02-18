# Vienna LaRose, Functions Notes Pyhton

#functions hold actions to be reused
#number = int(input("Please tell me a number:\n"))
def add(numOne, numTwo):#parameters set the name of the variable (just for the function)
    return numOne + numTwo

#print(add(number,21))#arguements set the value of the variable just for that instance of the function
#print(add(8,12))
#addition = add(6,4)
#print(add(addition,10000))
#add(87,3)

def values(type):
    return input(f"Please give me a {type}:\n")

name = values("name")
place = values("place")
verb = values("verb (past tense)")

print(f"{name} was really fast getting to {place} because they {verb} the whole way there.")