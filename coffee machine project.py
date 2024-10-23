# Program requirement
# 1. print report
# 2. check resources are sufficient
# 3. process coins
# 4. check transaction successful?
# 5. make coffee (deduct resources)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "capuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.8
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
# What would you like? (espresso/latte/cappuccino): report
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# What would you like? (espresso/latte/cappuccino): latte
# Please insert coins.
# How many quarters?: 
# How many dimes?:
# How many nickles?:
# How many pennies?:
# Here is $2.42 in change
# Here is your latte. Enjoy!
# What would you like?


def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"We do not have enough {item} for {drink}")
            return False
    print(f"We have enough resourcs for {drink}")
    for item in ingredients:
        # deduct resources
        resources[item] = resources[item] - ingredients[item]
    return True

def check_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total

def report_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")


machine_works = True
while machine_works==True:
    select = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if select == 'report':
        report_resources()
        money = check_coins()
        print(f"Coins: ${money:.2}")
    elif select in MENU:
        money = check_coins()
        check_resources(select)
        
    elif select == 'off':
        machine_works = False
        
