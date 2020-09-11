"""
Objectives
Write a program that offers to buy one cup of coffee or to fill the supplies or to take its money out. Note that the program 
is supposed to do one of the mentioned actions at a time. It should also calculate how many ingredients and money have left. 
Display the number of supplies before and after purchase.

1)First, your program reads one option from the standard input, which can be "buy", "fill", "take". If a user wants to buy some coffee, 
the input is "buy". If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be "fill". 
If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input "take".

2)If the user writes "buy" then they must choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino.

	For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
	For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
	And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. It costs $6.
	
3)If the user writes "fill", the program should ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine.

4)If the user writes "take" the program should give all the money that it earned from selling coffee.

At the moment, the coffee machine has $550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups.
"""


water = 400 
milk = 540
beans = 120
cups = 9
money = 550

def supplies():
    ''' State current level of supplies in the machine ''' 
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
    ''' Process user input to one of 3 primary requests ''' 
    request = input("Write action (buy, fill, take):")
    
    if request == 'buy':
        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        if coffee_type == '1':
            buy(1)
        elif coffee_type == '2':
            buy(2)
        elif coffee_type == '3':
            buy(3)
    
    elif request == 'fill':    
        fill()   
        
    elif request == 'take':
        take()
        
        
def buy(coffee_type):
    ''' Process type of coffee and how this updates the machine's supplies ''' 
    global water
    global milk
    global beans
    global cups
    global money
    
    if coffee_type == 1:
        water = water - 250
        beans = beans - 16
        money = money + 4 
        cups = cups - 1
        print(supplies())
    elif coffee_type == 2:
        water = water - 350
        milk = milk - 75
        beans = beans - 20
        money = money + 7
        cups = cups - 1
        print(supplies())
    elif coffee_type == 3:
        water = water - 200
        milk = milk - 100
        beans = beans - 12
        money = money + 6
        cups = cups - 1
        print(supplies())


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

    print(supplies())
    

def take():
    ''' Withdraw all money from the machine '''
    global money
    
    print("I gave you %d money" % (money))
    money = 0
    print(supplies())

print(supplies())
request()