# Vienna LaRose, Financial Calculator Update python
def info(cost, income, type):
    percent = cost/income *100
    print(f"Your {type} is ${cost:.2f} which is {percent}% of your income.")

# print statment that welcomes user and tells what program does
print("Welcome to my calculator that will help you manage your monthly finances.")
# ask what their income is (varible an input)
income = float(input("What is your income?\n"))
# ask what their rent is (varible an input)
rent = float(input("What is your rent?\n"))
# ask what their utlitites is (varible an input)
utlitites = float(input("What is your utlitites?\n"))
# ask what their groceries is (varible an input)
groceries = float(input("What is your groceries?\n"))
# ask what their transportation is (varible an input)
transportation = float(input("What is your transportation?\n"))
# calculate savings as 10% of income (income*.1) (variable)
savings = income *.1
# calculate spening as income-savings-rent-utilites-groceries-transportation (variable)
spending = income-savings-rent-utlitites-groceries-transportation

info(rent, income, "rent")
info(utlitites, income, "utlitites")
info(groceries, income, "groceries")
info(transportation, income, "transportation")
info(savings, income, "savings")
info(spending, income, "spending")