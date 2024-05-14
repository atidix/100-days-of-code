from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = Menu()
my_machine = CoffeeMaker()
my_money = MoneyMachine()

def my_coffee_machine():
    my_coffee = input(f"Which coffee would you like: {coffee.get_items()}: ")
    if my_coffee == "report":
        my_machine.report()
        my_money.report()
        my_coffee_machine()

    else:
        my_menu = coffee.find_drink(my_coffee)
        if my_menu != None:
            check = my_machine.is_resource_sufficient(my_menu)
            if check == True:
                my_money.make_payment(my_menu.cost)
                my_machine.make_coffee(my_menu)
                my_coffee_machine()

my_coffee_machine()

    

