# # This is my first Python program
# print("I like pizza!")
# print("It's really good!")
# first_name = "Rukawa"
# food = "Pizza"
# email = "Bro123@fake.com"

# #Intergers
# age = 25
# quantity =3
# num_of_students = 30

# print(f"You are {age} years old")
# print(f"You are buying {quantity} items")

# # Float
# price = 10.99

# print(f"The price is ${price}")

# # Boolean

# is_student = True

# print(f"Are you a student?: {is_student}")

# friends = 10

# friends = friends + 1
#friends += 1
#friends = friends - 2
#friends -= 2
#friends = friends *3
#friends* = 3
#friends = friends/ 2
#friends /= 2
#friends = friends **2
#friends **= 2
#remainder = friends % 2
# print(remainder) 

# x = 3.14
# y = 4
# z = 5

# result = round(x)
# result = abs(y)
# result = pow(y, 3)
# result = max(x, y, z)
# result = min(x, y, z)


# print(result)

# import math

# x = 9.9
# # print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

# print(result)

# import math
# radius = float(input("what is the radius: "))
# circumference = (2 * math.pi * radius)
# print(circumference)

# import math
# radius = float(input("what is the radius: "))
# result = (f"The area is: {round(math.pi * radius ** 2, 2)} cm^2")
# print(result)

# import math
# radius = float(input("What is the radius?: "))
# # if radius >= 10:
# #     result1 = float(round(math.pi* pow(radius,2), 1))
# #     print(f"The area is {result1} cm^2")
# # else:
# #     result2 = float(round(2*math.pi*radius,3))
# #     print(f"The circumference is {result2} cm")

# # response = input("Would you like food? (Y/N): ")

# # if response == "Y":
# #     print("Have some food!")
# # else:
# #     print("No food for you!")

# # unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# # temp = float(input("Enter the temperatue: "))

# # if unit == "C"

# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result, 3))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result, 3))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result, 3))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result, 3)) 
# else:
#     print(f"{operator} is not a valid operator")

#weight converter
# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     result = weight * 2.205
#     new_unit = "Lbs."
#     print(f"Your weight is : {round(result, 3)} {new_unit}")
# elif unit == "L":
#     result = weight / 2.205
#     new_unit = "Kgs."
#     print(f"Your weight is : {round(result, 3)} {new_unit}")
# else: 
#     print(f"{unit} was not valid")

# #temperature conversion
# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))

# if unit == "C":
#     temp = round((9 * temp)/5 +32, 1)
#     print(f"The temperature in Fahrenheit is : {temp}°F")
# elif unit == "F":
#     temp = round((temp - 32)*5 / 9, 1)
#     print(f"The temperature in Celsius is : {temp}°C")
# else:
#     print(f"{unit} is an invalid of measurement")

# logical operator = evaluate multiple conditions (or, and, not)
# or = at least one condition must be True
# and = both conditions must be True
# not = inverts the condition (not False, not True)

# # or
# temp = 20
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:   #if one of these conditions is true, then you can consider entire statement is true
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")

# #and, not
# temp = 0
# is_sunny = False

# if temp >= 28 and is_sunny:
#     print("It is HOT outside")
#     print("It is SUNNY")
# elif temp <= 0 and is_sunny:
#     print("It is COLD outside")
#     print("It is SUNNY")   
# elif 28 > temp > 0 and is_sunny:
#     print("It is WARM outside")
#     print("It is SUNNY")  
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside")
#     print("It is CLOUDY")
# elif temp <= 0 and not is_sunny:
#     print("It is COLD outside")
#     print("It is CLOUDY")   
# elif 28 > temp > 0 and not is_sunny:
#     print("It is WARM outside")
#     print("It is CLOUDY")    

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#Print or assign one of two values based on a condition X if condition else Y
# #example of print
# num = -5

# print ("Positive" if num > 0 else "Negative")

#example of assign
# num = 5 
# result ="EVEN" if num % 2 == 0 else "ODD"
# print(result)
# num = 5 
# a = 6
# b = 7
# age = 15
# temperature = 30
# user_role = "admin"

# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "Full Access" if user_role == "admin" else "Limited Access"

# print(access_level)

# name = input("Enter your full name: ")

# result = len(name)

# print(result)
# name = input("Enter your full name: ")

# result = name.find("e")
# result = name.rfind("q")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit() is a boolean
# result = name.isalpha() is a boolean

# print(result)

# phone_number = input("Enter your phone #: ")

# result = phone_number.count("-")

#replace method
# phone_number = phone_number.replace("-", " ")
# phone_number = phone_number.replace("-", "")


# print(phone_number)

#if you want a comprehensive(ครอบคลุม) list of all of the string method
#use print(help(str))
# print(help(str))

#validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

# username = input("Enter a username: ")

 
# if len(username) > 12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:         #if username.find("x") หาxไม่เจอ จะขึ้นเป็น -1 ดังนั้น if not แปลว่า หาเจอ
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}")


# indexing = accessing elements of a sequence using[] (indexing operator)   [start : end : step]

creditcard_numeber = "1234-5678-9012-3456"

# print(creditcard_numeber[0])
# print(creditcard_numeber[:4])
# print(creditcard_numeber[5:9])
# print(creditcard_numeber[5:])
# print(creditcard_numeber[-1])



