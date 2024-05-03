from recipe import MENU, resources

global money_in_machine
money_in_machine = 0

coffee_machine = True

def print_report(resources, money_in_machine):        
            for key in resources:
                print(key, resources[key])
            print(f'Money ${money_in_machine}')
            coffee_machine = True

 
while coffee_machine:
   
    def which_coffee():
        coffee = input("Which coffee would you like? espresso/ latte/ cappuccino: ")
        if coffee == "report":
              print_report(resources, money_in_machine)
              return which_coffee()
        else:
            return coffee

    which_coffee = which_coffee()
    if which_coffee == "off":
            print("Goodbye")
            break        
    else:
            coffee_choice = which_coffee
        
    def check_resources(MENU, coffee_choice, resources):
            for key in resources:
                if resources[key] < MENU[coffee_choice]["ingredients"][key]:
                    print (f"Sorry there is not enough {key}")
                    return 0
                else:
                    return 1


    if check_resources(MENU, coffee_choice, resources) == 1:
            print(f"Please insert coins. Your drink costs ${MENU[coffee_choice]['cost']}")
            quarter_count = int(input("Please enter number of quarters: "))
            dime_count = int(input("Please enter number of dimes: "))
            nickel_count = int(input("Please enter number of dimes: "))
            penny_count = int(input("Please enter number of pennies: "))
            total_user_money = (quarter_count*0.25) + (dime_count*0.10) + (nickel_count*0.05) + (penny_count*0.01)
    else:
            coffee_machine = False
            break

    def check_transaction(MENU, total_user_money, coffee_choice):
            if MENU[coffee_choice]["cost"] > total_user_money:
                print(f"Sorry, you gave a total of ${total_user_money}. That's not enough money. Money refunded")
                return 0
            elif MENU[coffee_choice]["cost"] <= total_user_money:
                print(f"Here's ${round(total_user_money-(MENU[coffee_choice]['cost']), 2)} dollars in change.")
                return 1

    def make_coffee(coffee_choice, MENU, resources):
            for key in resources:
                resources[key] = resources[key] - MENU[coffee_choice]["ingredients"][key]

    if check_transaction(MENU, total_user_money, coffee_choice) == 1:
            make_coffee(coffee_choice, MENU, resources)
            print(f"Here's your {coffee_choice}! Enjoy!")
    else:
            coffee_machine = False
            break

    money_in_machine += MENU[coffee_choice]['cost']


        


                   
