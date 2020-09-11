"""
The final step of the project is to refactor the program using an overarching class.
"""
class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def display_action(self):
        """Display default start menu"""
        print("Write action (buy, fill, take, remaining, exit):")

    def user_request(self):
        """Process user input to one of 5 requests"""
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            user_action = input()
            if user_action == 'buy':
                coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                if coffee_type == '1':
                    self.buy(1)
                elif coffee_type == '2':
                    self.buy(2)
                elif coffee_type == '3':
                    self.buy(3)
                elif coffee_type == 'back':
                    print("Returning to main menu")
            elif user_action == 'fill':
                self.fill_water()
                self.fill_milk()
                self.fill_beans()
                self.fill_cups()
            elif user_action == 'take':
                self.take()
            elif user_action == 'remaining':
                print(self.display_supply_levels())
            elif user_action == 'exit':
                break

    def buy(self, coffee_type):
        """Process type of coffee and how this updates the machine's supplies"""
        # Espresso
        if coffee_type == 1:
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough beans!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
                print("I have enough resources, making you a coffee!")
        # Latte
        elif coffee_type == 2:
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough water!")
            elif self.beans < 20:
                print("Sorry, not enough beans!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - 350
                self.milk = self.milk - 75
                self.beans = self.beans - 20
                self.money = self.money + 7
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")
        # Cappuccino
        elif coffee_type == 3:
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough water!")
            elif self.beans < 12:
                print("Sorry, not enough beans!")
            elif self.cups == 0:
                print("Sorry, not enough cups!")
            else:
                self.water = self.water - 200
                self.milk = self.milk - 100
                self.beans = self.beans - 12
                self.money = self.money + 6
                self.cups = self.cups - 1
                print("I have enough resources, making you a coffee!")

    def display_fill_message(self, resource, measure):
        """Used in fill methods to question amount desired to add"""
        print("Write how many {} of {} do you want to add:".format(measure, resource))

    """All methods below fill the related supply; these could all be one function but I felt having them separate had better readability."""
    def fill_water(self):
        self.display_fill_message("water", "ml")
        d_water = int(input())
        self.water += int(d_water)
        
    def fill_milk(self):
        self.display_fill_message("milk", "grams")
        d_milk = int(input())
        self.milk += int(d_milk)
        
    def fill_beans(self):
        self.display_fill_message("coffee beans", "grams")
        d_beans = int(input())
        self.beans += int(d_beans)
        
    def fill_cups(self):
        self.display_fill_message("coffee", "disposable cups")
        d_cups = int(input())
        self.cups += int(d_cups)
        
    def take(self):
        ''' Withdraw all money from the machine '''
        print("I gave you %d money" % (self.money))
        self.money = 0

    def display_supply_levels(self):
        print("The coffee machine has:")
        print(str(self.water) + " of water")
        print(str(self.milk) + " of milk")
        print(str(self.beans) +  " of coffee beans")
        print(str(self.cups) + " of disposable cups")
        print(str(self.money) + " of money")

coffee_machine = CoffeeMachine()
coffee_machine.user_request()
