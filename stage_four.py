"""
Objectives
Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. 
Introduce two new options: "remaining" and "exit".

Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, 
the program should output a message that says it can't make a cup of coffee.

And the last improvement to the program at this step — if the user types "buy" to buy a cup of coffee and then changes his mind, 
they should be able to type "back" to return into the main cycle.
"""

looping = True # keep while loop until user enters 'exit'

water = 400 
milk = 540
beans = 120
cups = 9
money = 550


def supplies():
    ''' State current level of supplies in the machine ''' 
    global looping
    global water
    global milk
    global beans
    global cups
    global money
    
    print("The coffee machine has:")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(beans) +  " of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")
    
def request():
    global looping
    
    ''' Process user input to one of 3 primary requests ''' 
    request = input("Write action (buy, fill, take, remaining, exit):")
    
    if request == 'buy':
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee_type == '1':
            buy(1)
        elif coffee_type == '2':
            buy(2)
        elif coffee_type == '3':
            buy(3)  
        elif coffee_type == 'back':
            print("Returning to main menu")
            
    elif request == 'fill':    
        fill()         
    elif request == 'take':
        take()  
    elif request == 'remaining':
        print(supplies()) 
    elif request == 'exit':
        looping = False
        
def buy(coffee_type):
    ''' Process type of coffee and how this updates the machine's supplies ''' 
    global water
    global milk
    global beans
    global cups
    global money
    
    if coffee_type == 1:   
        if water < 250:
            print("Sorry, not enough water!")  
        elif beans < 16:
            print("Sorry, not enough beans!")        
        elif cups == 0:
            print("Sorry, not enough cups!")
        else:     
            water = water - 250 
            beans = beans - 16
            cups = cups - 1  
            money = money + 4 
            print("I have enough resources, making you a coffee!")
        
    elif coffee_type == 2:       
        if water < 350:
            print("Sorry, not enough water!")  
        elif milk < 75:
            print("Sorry, not enough water!")        
        elif beans < 20:
            print("Sorry, not enough beans!")
        elif cups == 0:
            print("Sorry, not enough cups!")
        else:
            water = water - 350 
            milk = milk - 75
            beans = beans - 20
            money = money + 7   
            cups = cups - 1  
            print("I have enough resources, making you a coffee!")
        
    elif coffee_type == 3:
        if water < 200:
            print("Sorry, not enough water!")   
        elif milk < 100:
            print("Sorry, not enough water!")        
        elif beans < 12:
            print("Sorry, not enough beans!")    
        elif cups == 0:
            print("Sorry, not enough cups!")
        else:
            water = water - 200
            milk = milk - 100
            beans = beans - 12
            money = money + 6
            cups = cups - 1
            print("I have enough resources, making you a coffee!")


def fill():
    ''' Take inputs to increase machine supplies '''
    global water
    global milk
    global beans
    global cups
    global money

    dwater = input("Write how many ml of water do you want to add:")
    water = water + int(dwater)
    
    dmilk = input("Write how many ml of milk do you want to add:")
    milk = milk + int(dmilk)
    
    dbeans = input("Write how many grams of coffee beans do you want to add:")
    beans = beans + int(dbeans)
    
    dcups = input("Write how many disposable cups of coffee do you want to add:")
    cups = cups + int(dcups)
    

def take():
    ''' Withdraw all money from the machine '''
    global money
    
    print("I gave you %d money" % (money))
    money = 0


# Main loop for machine
while looping:
    request()