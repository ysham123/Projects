import time

#TODO Coffee recipes
recipes = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#TODO Inventory
inventory = {
    "water": 1000,  # in ml
    "milk": 500,    # in ml
    "coffee": 100,  # in grams
}

#TODO Function to check if enough resources are available to make the drink
def can_make_drink(drink_name):
    if drink_name in recipes:
        for ingredient, amount in recipes[drink_name]["ingredients"].items():
            if inventory[ingredient] < amount:
                return False
        return True
    else:
        return False

#TODO Function to process the coins inputted and check if it's enough
def grab_money_from_user(drink_name, input_money):
    if drink_name in recipes:
        drink_cost = recipes[drink_name]["cost"]
        if input_money >= drink_cost:
            change = input_money - drink_cost
            return True, change  # Return True and the change to be given back
        else:
            remaining = drink_cost - input_money
            return False, remaining  # Return False and the remaining amount needed
    else:
        return False, None  # If the drink is not on the menu

def get_additional_money(initial_money, required_money):
    start_time = time.time()
    total_money = initial_money
    while total_money < required_money:
        # Check if 5 seconds have passed
        if time.time() - start_time > 5:
            print("Transaction timed out.")
            return total_money

        print(f"Additional money needed: ${required_money - total_money:.2f}")
        try:
            additional_money = float(input("Insert additional money: "))
            total_money += additional_money
        except ValueError:
            print("Invalid input. Please insert valid amount.")

    return total_money

#TODO Main interaction with the user
order = input("What would you like to order today? We have Espresso, Latte, and Cappuccino:\n").lower()
if can_make_drink(order):
    input_money = float(input("Please insert money: "))
    success, change_or_remaining = grab_money_from_user(order, input_money)
    if not success:
        print(f"Insufficient funds. Total inserted: ${input_money:.2f}")
        total_money = get_additional_money(input_money, recipes[order]["cost"])
        success, change_or_remaining = grab_money_from_user(order, total_money)

    if success:
        print(f"Thank you! Here is your {order.capitalize()} and your change: ${change_or_remaining:.2f}")
    else:
        print("Transaction not completed.")
else:
    if order in recipes:
        print("Sorry, we cannot make that drink due to lack of ingredients.")
    else:
        print("Sorry, we do not have that drink on our menu.")



#TODO: Make the Coffee
def coffee_made():
    print("Making your coffee...")
    time.sleep(5)  # Wait for 5 seconds
    print("Here is your Coffee! Enjoy!.")
