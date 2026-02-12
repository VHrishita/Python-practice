""" total = 0
choice = "y"
name = input("Enter your name:")
print("Welcome",name,"!")
age = int(input("Enter your age:"))
print("You are", age, "years old!")
while choice == "y":
    product=input("Enter the product name:")
    print("You added", product, "to cart!")
    units=int(input("Enter the number of units needed:"))
    print("Added", units, "units of", product)
    price=float(input("Enter the amount paid for products:"))
    print("You paid", price, "rupees")
    total = total+price
    choice2 = input("Do you wanna continue shopping? (y/n)")
    if choice == "n":
    print("Your total:", total)
    print("Thank you for shopping with us!")
else:
    print("Invalid! Please enter (y) or (n)")

print("Have a nice day!") """

total = 0
choice = "y"

name = input("Enter your name: ")
print("Welcome", name, "!")

age = int(input("Enter your age: "))
print("You are", age, "years old!")

while choice == "y":
    product = input("Enter the product name: ")
    print("You added", product, "to cart!")

    units = int(input("Enter the number of units needed: "))
    print("Added", units, "units of", product)

    price = float(input("Enter the amount paid for products: "))
    print("You paid", price, "rupees")

    total = total + price

    choice = input("Do you wanna add more products? (y/n) : ")
    if choice == "n":
        print("Your total:", total)
    else:
        print("Invalid! Please enter (y or n)")
print("Thank you for shopping with us!")
print("Have a nice day!")
