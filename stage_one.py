"""
Let's break the task into several steps:

First, read the numbers of coffee drinks from the input.
Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains 200 ml of water, 50 ml of milk, and 15 g of coffee beans.
Output the required ingredient amounts back to the user.
"""

cups = int(input("Write how many cups of coffee you will need:"))
response = "For {} cups of coffee you will need:".format(str(cups))
print(response)

water = cups * 200
milk = cups * 50
beans = cups * 15

print(str(water) + " of water")
print(str(milk) + " of milk")
print(str(beans) + " of coffee beans")
