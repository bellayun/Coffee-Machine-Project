# Program requirement
# 1. print report
# 2. check resources are sufficient
# 3. process coins
# 4. check transaction successful?
# 5. make coffee (deduct resources)

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

from machine_data import MENU, resources

# check how much resources in the machine, and deduct right amount depending on the drink you choose
def check_resources(drink):
    ingredients = MENU[drink]['ingredients']
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"We do not have enough {item} for {drink}")
            return False
    print(f"We have enough resourcs for {drink}")
    # Deduct the resources for the drink    
    for item in ingredients:
        # deduct resources
        resources[item] -= ingredients[item]
    return True

# check how much money is inserted
def check_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    return total

# Deduct the cost of the drink from the total money and return the remaining balance
def deduct_coins(drink, total_amount):
    cost = MENU[drink]['cost']
    if total_amount >= cost:
        remaining_money = total_amount
        print(f"Drink cost ${cost:.2f}. You have ${remaining_money:.2f} left.")
        return remaining_money
    else:
        print(f"Not enough money. {drink} costs ${cost:.2f}.")
        return total_amount

# report resources in the coffee machine
def report_resources(money):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


########## main ##########
money = 0
machine_works = True

while machine_works==True:
    select = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if select == 'report':
        report_resources(money)
    elif select in MENU:
        inserted_money = check_coins()    # Get total inserted money
        money += inserted_money    # Add inserted money to total
        
        #TypeError, because you're trying to add `inserted_money`, but instead of calling the `check_coins()` function, you're assigning it directly as `check_coins`, which is a reference to the function itself, not the result of the function call.
        if check_resources(select):
            money = deduct_coins(drink=select, total_amount=money)
        else:
            print("Not enough resources for your drink. Refunding money.")
    elif select == 'off':
        machine_works = False
        
