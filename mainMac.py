# import math

# # Strings
# first_name ="Rio"
# food = "pizza"
# email = "maki@hi.com"
# print(f"Your email is {email}")
# # Integers
# age = 20
# print(f"Your age is {age}")
# # Float
# price = 19.99
# print(f"The price is {price}")
# # Boolean
# is_active = True

# if is_active:
#     print("The account is active.")
# else:
#     print("The account is inactive.")

# test = input("Press Enter to exit...")
# print(f"Hello {test}")

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
# area = math.ceil(length * width)
# print(f"The area is {area}")

# perimeter = math.ceil( 2 * (length + width) )
# print(f"The perimeter is {perimeter}")

# num = 5
# num += 10
# print(f"The updated number is {num}")
# result = round(x)
# result = abs(y)
# result = pow(x, 4)
# result = max(x, y, z)
# result = min(x, y, z)

# str() int() float() bool()

# age = int(input("Enter your age: "))

# if age >=18:
#     print("You are an adult.")
# elif age >= 13:
#     print("You are a teenager.")
# else:
#     print("You are a child.")
# adapt = "Yes"
# if adapt == "Yes":

# print("Hello")

# credit_number = "1234-5678-9012-3456"

# # last_digits = credit_number[-4:]
# # print(f"xxxx-xxxx-xxxx-{last_digits}")

# credit_number = credit_number[::-1] # Reversing the string
# print(credit_number)

# format specifiers = {value:flags} format a value based on what flags are inserted

# price1 = 18.992765

# print(f"Price 1 is ${price1:+,.2f}")

# while loop = execute some code WHILE some condition remains true

# name = input("Enter your name:  ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name:  ")
# print(f"Hello {name}")

# age = int(input("Enter your age: "))

# while age < 0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))

# print(f"You are {age} years old")

# food = input("Enter a food you like (q to quit):  ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit):  ")

# print("bye")

# num = int(input("Enter a # between 1 - 10:  "))

# while num < 1 or num > 10:
#     print(f"{num} is not valid")
#     num = int(input("Enter a # between 1 - 10:  "))

# print(f"Your number is {num}")

# Python compound intereset calculator

# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter the priniciple amount: "))
#     if principle < 0:
#         print("Priniciple can't be less than zero")
#     else:
#         break

# while True:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than zero")
#     else:
#         break
# while True:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than zero")
#     else:
#         break

# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time}m year/s: ${total:.2f}")

# for loop = execute a block of code a fixed number of times. You can iterate over a range, string, sequence, etc.

# for x in range(1, 11):
    # print(x)


# for x in range(1, 11, 2):
#     print(x)

# print("HAPPY NEW YEAR!")

# for x in range(1,21):
#     if x == 13:
#         continue
#     else:
#         print(x)


# import time

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60 # % is the modulus operators gives you the remainder of any division
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600) 
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")

# nested loop = A loop within another loop (outer, inner)
#outer loop:
#   inner loop:


# rows = int(input("Enter the # of rows: "))
# columns = int(input("Enter the # of columns: "))
# symbol = input("Enter a symbol to use: ")


                 

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()

# collection = single "variable" used to store mulitple values
# List = [] ordered and changealbe. Duplicates OK
# Set = {} unordered and immutable, but Add/ Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[1] = "pineapple"
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(2, "pineapple")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("orange"))
# print(fruits.count("banana"))


# print(fruits)
# for fruit in fruits:
    # print(fruit)

# fruits = {"apple", "orange", "banana", "coconut", "coconut"}
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()
# fruits.clear()


# print(fruits)

# fruits = ("apple", "orange", "banana", "coconut", "coconut")
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits.index("banana"))
# print(fruits.count("coconut"))

# print(fruits)
# for fruit in fruits:
    # print(fruit)

# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else: 
        price = float(input(f"Enter the price of a {food}:  $"))
        foods.append(food)
        prices.append(price)
    
print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price #+= coming from, total = total + price

print()
print(f"Your total is: ${total}")
