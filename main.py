"""
Made by Ryan Wilson
https://github.com/onlinePB
"""

# Importing modules
from userInput import *
from income import *
from fileHandler import *

# Initialising variables
incomeMethods = []
expenses = []
running = True

# Credits
print("=== [ ABOUT ]===\nFinance Calculator v1.0.0\nMade by Ryan Wilson (github.com/onlinePB)\nReport bugs at https://github.com/onlinePB/finance-calculator/issues\n© Ryan Wilson 2019. All rights reserved.")
input("\nPress Enter to continue...")

while running:
    # ========== GET CURRENCY SYMBOL
    userCurrency = str(input("\nWhat symbol would you like to use for currency?\nCurrency symbol: "))

    # ========== COLLECT INCOME METHODS
    collectingIncomeMethods = True
    print("\n===[ INCOME METHODS ]===")
    while collectingIncomeMethods:
        incomeName = str(input("Enter the name of this income method:\n"))
        incomeAmount = UserInput.getFloat("Enter the amount you make per month through this method:\n" + userCurrency)
        incomeMethods.append(Income(incomeName, round(incomeAmount, 2)))

        if not UserInput.yesOrNo("Do you want to add another income method?\n[Y]es or [N]o: "):
            collectingIncomeMethods = False

    # ========== COLLECT EXPENSES
    collectingExpenses = True
    print("\n===[ EXPENSES ]===")
    while collectingExpenses:
        expenseName = str(input("Enter the name of this expense:\n"))
        expenseAmount = -UserInput.getFloat("Enter the amount you spent per month on this expense:\n" + userCurrency)
        expenses.append(Income(expenseName, round(expenseAmount, 2)))

        if not UserInput.yesOrNo("Do you want to add another expense?\n[Y]es or [N]o: "):
            collectingExpenses = False

    # ========== GET TOTALS
    incomeTotal = 0
    expenseTotal = 0

    for method in incomeMethods:
        incomeTotal += method.getAmountMonthly()

    for expense in expenses:
        expenseTotal += expense.getAmountMonthly()

    netProfit = incomeTotal + expenseTotal

    # ========== GET PERCENTAGES
    incomePercentages = []
    expensePercentages = []

    for method in incomeMethods:
        incomePercentages.append(round((method.getAmountMonthly() / incomeTotal)*100, 2))

    for expense in expenses:
        expensePercentages.append(round((expense.getAmountMonthly() / expenseTotal)*100, 2))

    # ========== FORMAT FOR CSV
    # Add income header and income methods
    data = [["INCOME METHOD", "AMOUNT (" + userCurrency + ")", "PERCENTAGE"]]
    for i in range(len(incomeMethods)):
        data.append([incomeMethods[i].getName(), incomeMethods[i].getAmountMonthly(), str(incomePercentages[i]) + "%"])

    # Add income total and expense header
    data.append(["", "", ""])
    data.append(["Total:", incomeTotal, "100%"])
    for i in range(2):
        data.append(["", "", ""])
    data.append(["EXPENSE", "AMOUNT (" + userCurrency + ")", "PERCENTAGE"])

    # Add expenses
    for i in range(len(expenses)):
        data.append([expenses[i].getName(), expenses[i].getAmountMonthly(), str(expensePercentages[i]) + "%"])

    # Add expense total and net profit
    data.append(["","",""])
    data.append(["Total:", expenseTotal, "100%"])
    for i in range(2):
        data.append(["", "", ""])
    data.append(["Net profit:", round(netProfit, 2), ""])

    # ========== GET FILENAME AND EXPORT
    print("\n===[ EXPORTING FILE ]===")
    FileHandler.export(UserInput.getFileName("What would you like to call your spreadsheet?\nFile name: "), data)
    print("Exported successfully!")

    # ========== ASK IF THEY'D LIKE TO MAKE ANOTHER
    if not UserInput.yesOrNo("\nWould you like to make another spreadsheet?\n[Y]es or [N]o: "):
        running = False
        
print("\nGoodbye!")
