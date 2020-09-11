"""
Objectives
Write a program that does the following:

1)It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.

2)If the coffee machine has enough supplies to make the specified amount of coffee, the program should print "Yes, I can make that amount of coffee".

3)If the coffee machine can make more than that, the program should output "Yes, I can make that amount of coffee (and even N more than that)", 
where N is the number of additional cups of coffee that the coffee machine can make.

4)If the amount of given resources is not enough to make the specified amount of coffee, the program should output "No, I can make only N cups of coffee".

Like in the previous stage, the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.
"""

# the coffee machine needs 200 ml of water, 50 ml of milk, and 15 g of coffee beans to make one cup of coffee.
water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:"))

cups = int(input("Write how many cups of coffee you will need:"))

# n stands for needed
n_water = cups * 200
n_milk = cups * 50
n_beans = cups * 15

# p stands for possible
p_water = water // 200
p_milk = milk // 50
p_beans = beans // 15

maximum_cups = min(p_water, p_milk, p_beans)

if maximum_cups == cups:
    print("Yes, I can make that amount of coffee")
elif maximum_cups >= 2 and maximum_cups > cups:
    print("Yes, I can make that amount of coffee (and even %d more than that)" % (maximum_cups-1))
elif maximum_cups < cups:
    print("No, I can make only %d cups of coffee" % (maximum_cups))
    