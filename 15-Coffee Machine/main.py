# Day 15 Project: Coffee machine project

"""this statement imports coffee module"""
import coffee

"""this statement prints coffee logo from the coffee module"""
print(coffee.logo)

"""this function generates report of the resources left and the profit made"""
def report():
    for resource in coffee.resources:
        if (resource != "coffee"):
            print(f"{resource}: {coffee.resources[resource]}ml")
        else:
            print(f"{resource}: {coffee.resources[resource]}g")
    print(f"Money: ${coffee.profit}")

"""this function calulates if there is sufficient resources to make the required coffee"""
def resourcesSufficient(coffeeIngredients, resources):
    for ingredient in coffeeIngredients:
        if (coffeeIngredients[ingredient] > resources[ingredient]):
            print(f"Sorry there is not enough {ingredient}")
            return False
        else:
            return True

"""this function proccesses coins and returns the total value in dollars"""
def processCoins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    totalValue = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickels) + (0.01 * pennies)

    return totalValue

"""this function does the transaction and returns the balance money to the user or 
refunds if the money is not enough to make the required coffee"""
def transaction(coffeeCost):
    userMoney = processCoins()
    if (userMoney < coffeeCost):
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        return userMoney - coffeeCost
    
"""this function makes the coffee if there is sufficient resources as well as the cost of 
the coffee provided by the user is enough"""
def makeCoffee(coffeeIngredients, resources):
    for ingredient in coffeeIngredients:
        resources[ingredient] -= coffeeIngredients[ingredient]
    

"""iniitially the machine is on and the user has not done a exit"""
machineExit = False
"""until the user has not done a exit the coffee machine will run"""
while (machineExit == False):
    coffeeMachineCommand = input("What would you like? (espresso / latte / cappuccino): ")
    if (coffeeMachineCommand == "report"):
        report()
    elif (coffeeMachineCommand == "exit"):
        machineExit = True
    elif (coffeeMachineCommand == "espresso" or coffeeMachineCommand == "latte" or coffeeMachineCommand == "cappuccino"):
        if (resourcesSufficient(coffeeIngredients = coffee.MENU[coffeeMachineCommand]["ingredients"], resources = coffee.resources) == True):
            changeMoney = transaction(coffee.MENU[coffeeMachineCommand]["cost"])
            if (changeMoney):
                coffee.profit += coffee.MENU[coffeeMachineCommand]["cost"]
                print(f"Here is ${round(changeMoney, 2)} dollars in change.")
                makeCoffee(coffeeIngredients = coffee.MENU[coffeeMachineCommand]["ingredients"], resources = coffee.resources)
                print(f"Here is your {coffeeMachineCommand}. Enjoy!")

            
            

