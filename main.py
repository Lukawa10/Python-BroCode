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

# creditcard_numeber = "1234-5678-9012-3456"

# # print(creditcard_numeber[0])
# # print(creditcard_numeber[:4])
# # print(creditcard_numeber[5:9])
# # print(creditcard_numeber[5:])
# # print(creditcard_numeber[-1])


# print("Hello")

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

# Python compound intereset calculator ซึ่งไม่สามารถใส่ค่า 0 ได้ ในเครื่องคิดเลข

# principle = 0
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the priniciple amount: "))
#     if principle < 0:
#         print("Priniciple can't be less than or equal to zero")

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate < 0:
#         print("Interest rate can't be less than or equal to zero")

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time < 0:
#         print("Time can't be less than or equal to zero")

# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time}m year/s: ${total:.2f}")

# Python compound intereset calculator อันนี้สามารถใส่ค่า 0 ได้ ในเครื่องคิดเลข

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
#ใช้เกี่ยวกับ loop ที่เป็น fixed number of times

# for x in range(1, 11):
    # print(x)


# for x in range(1, 11, 2):
#     print(x)

# print("HAPPY NEW YEAR!")

# for x in range(1,21): ข้ามเลข 13
#     if x == 13:
#         continue
#     else:
#         print(x)

# for x in range(1,21): หยุดที่เลย 13
#     if x == 13:
#         break
#     else:
#         print(x)

##import time ใช้สร้าง countdown timer

# import time
# time.sleep(3)

# print("TIME'S UP!")

# my_time = int(input("Enter the time in seconds: "))

# for x in range(my_time, 0, -1):
#     seconds = x % 60 # % is the modulus operators gives you the remainder of any division
#     minutes = int(x / 60) % 60
#     hours = int(x / 3600) 
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)

# print("TIME'S UP!")

# nested loop = A loop within/inside of another loop (outer, inner)
#outer loop:
#   inner loop:

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")

# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")  ##end="" to make the code end in the same line with empthy string
#     print()    ## print a new line then repeat it all over again until the outer loop is satisfied



# rows = int(input("Enter the # of rows: "))  ##จำนวนรอบที่ line จะซ้ำกันของ outer loop or rows
# columns = int(input("Enter the # of columns: "))  ##in charge of columns
# symbol = input("Enter a symbol to use: ")


# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()


# collection = single "variable" used to store mulitple values
# List = [] ordered and changealbe. Duplicates OK
# Set = {} unordered and immutable, but Add/ Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut"]  ## this is List that are ordered and changealbe Duplicates OK
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits[1] = "pineapple"
# fruits.append("pineapple")     ##to add an element to the end of a list
# fruits.remove("apple")         ## to remove an element
# fruits.insert(2, "pineapple")  ## to insert value at the given index
# fruits.sort()                  ##to sort the list of element in an alphabet order
# fruits.reverse()               ## to reverse based on what we place them
# fruits.clear()                 ## clear all elements
# print(fruits.index("orange"))
# print(fruits.count("banana"))


# print(fruits)
# for fruit in fruits:
    # print(fruit)

# fruits = {"apple", "orange", "banana", "coconut", "coconut"}  ## this is Set the set is unordered from originally, but Add/ Remove OK. NO duplicates
# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.pop()    ## will remove whatever element is first which is also randomly select to be first to remove
# fruits.clear()  ## clear all elements


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

# List = [] ordered and changealbe. Duplicates OK
# Set = {} unordered and immutable, but Add/ Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# foods = []
# prices = []
# total = 0

# while True:
#     food = input("Enter a food to buy (q to quit): ")
#     if food.lower() == "q":                        # พอเราเพิ่ม .lower มา this will make our input make it lowercase ทันที automatic
#         break
#     else: 
#         price = float(input(f"Enter the price of a {food}:  $"))
#         foods.append(food)
#         prices.append(price)
    
# print("----- YOUR CART -----")

# for food in foods:
#     print(food, end=" ")   ##พอมี end=" " to make the code end in the same line with one space gap

# for price in prices:
#     total += price       ## += coming from, total = total + price

# print()  ##print() is using for making a new row of line
# print(f"Your total is: ${total}")







# #2D list is a list made up of list, its useful when you need matrix of data(kinda like excel spreadsheet)
# # First we create a lists that each lists is a one-dimensional list, to create a two-dimensional list.
# #we also need to lay out the list to make it similar/resembles a row of the matrix and each element similar/resembles to a column
# fruits =     ["apple", "orange", "banana", "coconut"]
# vegetables = ["celery", "carrots", "potatoes"]
# meats =      ["chicken", "fish", "turkey"]

# #to create a two-dimensional list, you would begin by creating a one-dimensional list.
# #Let's create a list of groceries, by add all our individual lists as elements to the outer list(the 2D list)
# groceries = [fruits, vegetables, meats]

# print(groceries[0])     #this, print(groceries[0]), will return the entire first row instead of first element
# print(groceries[0][0])  # ex this, print(groceries[1][0]) is to specific to a first element in the second row the matrix

# #we can even do this instead too
# groceries = [["apple", "orange", "banana", "coconut"], 
#              ["celery", "carrots", "potatoes"], 
#              ["chicken", "fish", "turkey"]]
# print(groceries[0][0]) 


# ##if you ever need to iterate/ทำซ้ำ over the elements of a 2D, you can use nested loops.
# groceries = [["apple", "orange", "banana", "coconut"], 
#              ["celery", "carrots", "potatoes"], 
#              ["chicken", "fish", "turkey"]]
# ##using a single for loop would iterate/ทำซ้ำ over the rows 
# # for collection in groceries:    
# #     print(collection)
# ##but to also iterate/ทำซ้ำ over the elements found within each row, we nested loop!! (aka for and for) to iterate/show over all elements in 2d list
# for collection in groceries:    
#     for food in collection:
#         print(food, end=" ")    ##พอมี end=" " to make the code end in the same line with one space gap
#     print()     ##print() is using for making a new row of line

##not only just for list[] but we also can tuple() too or set{}        # List = [] ordered and changealbe. Duplicates OK
                                                                       # Set = {} unordered and immutable, but Add/ Remove OK. NO duplicates
                                                                       # Tuple = () ordered and unchangeable. Duplicates OK. FASTER

##exercise create 2d keypad on your phone, we need to use ordered number so tuple or list?, answer we use tuple
## tuple because is ordered and unchangeable
#create 2d tuple
# num_pad =((1, 2, 3),
#           (4, 5, 6),
#           (7, 8, 9),
#           ("*", 0, "#"))  ##now num_pad is a 2d tuple, lets use it to iterate over every row
# # for row in num_pad:
# #     print(row)  ##printing every row in our numpad 
# ##but we want to remove () aka parenthesis so we use nested loop!!
# for row in num_pad:
#     for num in row:
#         print(num, end=" ")
#     print()


#ทวนความจำ!!!!!
#  nested loop = A loop within/inside of another loop (outer, inner)
#       outer loop:
#           inner loop:

#        for x in range(3):
#           for y in range(1, 10):
#               print(y, end="")
#            print()







# #create quiz game in python

# questions = ("How many elements are in the periodic table?: ",
#              "Which animal lays the largest eggs?: ",
#              "What is the most abundant gas in Earth's atmosphere?: ",
#              "How many bones are in the human body?: ",
#              "Which planet in the solar system is the hottest?: ")

# options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#            ("A. 206", "B. 207", "C. 208", "D. 209"),
#            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# answers = ("C", "D", "A", "A", "B")         # a tuple storing the correct answers
# guesses = []                                #stores all the user’s answers.
# score = 0                                   #starts the user’s score at zero and increases with each correct answer.
# question_num = 0                            #keeps track of the current question number being checked.

# ##First display each question. By iterate over tupple of questions.
# for question in questions:
#     print("----------------------")
#     print(question)
#     for option in options[question_num]:            #after we display every questions, we need to display every options. 
#         print(option)                               #option is a 2D tupple, so we need to add index operator (question_num = 0)
#         #but we need to have each specific options for each questions
#     #and before we iterating the question number, we will ask the user for the guess first!!!!!!
#     guess = input("Enter(A, B, C, D): ").upper()                          # .upper() is to make user input uppercase
#     guesses.append(guess)                          ##guesses.append(guess) adds the user’s current answer (guess) to the end of the guesses list, which stores all the player’s answers.
#     if guess == answers[question_num]:                     #since answers = ("C", "D", "A", "A", "B") then "question_num" keeps track of the current question 
#         score += 1                                         #, so for the first question (question_num = 0) it checks answers[0], for the second (question_num = 1) it checks answers[1], and so on.
#         print("CORRECT!")
#     else:
#         print("INCORRECT!")
#         print(f"{answers[question_num]} is the correct answer")
#     question_num += 1                                   #It’s shorthand for, question_num = question_num + 1

# #Once we complete all the questions, Let's print the result!
# print("----------------------")
# print("        RESULT        ")  #ส่วนนี้ไม่จำเป็นแค่เท่
# print("----------------------")

# print("answers:, ", end="")
# for answer in answers:
#     print(answer, end=" ")
# print()

# print("guesses:, ", end="")
# for guess in guesses:
#     print(guess, end=" ")
# print()

# score = int(score / len(questions) * 100)
# print(f"Your score is: {score}%")





# # dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates allow
# # dictionary is one of the four basic collection types for beginners. example for {key:value} could be an ID and Name, an item and a price.

# # but today we create a dictionary of countries and capitals city!
# capitals = {"USA": "Washington D.C.",               # we {"key":"value of the key"}       # we use set{}
#             "India": "New Delhi",
#             "China": "Beiging",
#             "Russia": "Moscow"}                                                   # List = [] ordered and changealbe. Duplicates OK"
#                                                                                   # Set = {} unordered and immutable, but Add/ Remove OK. NO duplicates
#                                                                                   # Tuple = () ordered and unchangeable. Duplicates OK. FASTER
# # print(dir(capitals))  
# # print(help(capitals))                                                                                  

# # Now to get one of the values from a dictionary, you would get the key. By type     .get("of the key value")
# # print(capitals.get("USA"))     #we will get Washington D.C. as we already put the vaule in the set{}
# # print(capitals.get("India"))     #we will get New Delhi as we already put the vaule in the set{}

# # if capitals.get("Japan"):               # Since Japan is not in our dicitionary, as we did not put Japan as a key in the set{}
# #     print("That capital exists")          
# # else:
# #     print("That capital doesn't exist")
    
# # if capitals.get("Russia"):               # Since Russia is in our dicitionary, as we put Russia as a key in the set{}
# #     print("That capital exists")          
# # else:
# #     print("That capital doesn't exist")

# #Now we will update our dicitonary
# # capitals.update({"Germany": "Berlin"})       # using .update method we can insert a new key value pair 
# # capitals.update({"USA": "Detroit"})             # or we can update/change the existing one in the list of dictionary  
# # capitals.pop("China")                        # use .pop method to remove a key value pair
# # capitals.popitem()                         #this will remove the lateset key value pair in the list
# # capitals.clear()                            # .clear is to clear everthing in the dictionary list
# # print(capitals)

# #to get all of the keys within the dictionary but not the value we use .keys method
# # keys = capitals.keys()

# # print(keys)         # the .keys method will return all of the keys within our dicitionary, as keys is an object which resembles a list

# #if you need the keys in a dictionary with a for loop as they're iterable
# # keys = capitals.keys()

# # for key in capitals.keys():     #for loop
# #     print(key)

# # there is also value method to get all values in a dictionary list by using .values method
# # values = capitals.values()
# # print(values)

# # now use the for loop to iterate and print over every value within our dictionary
# # for value in capitals.values():
# #     print(value)

# # item method
# # items = capitals.items()
# # print(items)
# #items will returns a dictionary object which resembles of a 2D list of tupple. aka [(), (), ()] 
 
# # and we use for loop to print every key, value in capitals.items():
# for key, value in capitals.items():
#     print(f"{key}: {value}")
# ## then we get 
# # USA: Washington D.C.
# # India: New Delhi
# # China: Beiging
# # Russia: Moscow






# # we will create a program to mimic a concession stand (ซุ้มขายอาหาร/เครื่องดื่ม)
# #we will utilizing a dixtionary to keep tack of a menu item and an associated price
# # dictionary {key:value}

# # first create dictionary named it menu
# menu = {"pizza": 3.00,
#         "nachos": 4.50,
#         "popcorn": 6.00,
#         "fries": 2.50,
#         "chips": 1.00,
#         "pretzel": 3.50,
#         "soda": 3.00,
#         "lemonade": 4.25,}
# # now we have menu, so user going to select specific keys from this menu
# # depending on what the key is, we can get the associated value to calculate a total.

# cart = []    # So to keep track of the user selected item, we will create an empty list named cart.
# total = 0    # we also declare a variable named total to keep track of the total.


# # we need to lay this dictionary down flat to display to the user by use for loop plus .item method
# print("-------- MENU --------")       #to decorate menu
# for key, value in menu.items():       # since .item method of our dictionary will returna key and a value during each iteration
#     print(f"{key:10}: ${value:.2f}")      # :10 is to allocate 10 spaces to จัดระเบียบ, while .2f is to display two decimal
# print("----------------------")       #to decorate menu


# #now we will ask a user for some input, what item would they like to buy from the menu?

# # while loop aka. while True: loop is an infinite loop — it keeps running forever unless you use a break statement (or stop the program).
# while True:           #while our condition will be true, if our condition is set to true, we'll need to break out of this loop 
#     food = input("Select an item (q to quit): ").lower()       #we will Keeps asking the user to pick something by write the input
#     if food == "q":                                            # .lower()  is to make all user input and make it all lowercase
#         break                 #If the user types q, the loop stops.
#     elif menu.get(food) is not None:      #this is Step: Check and add item, menu.get(food) checks if the item is in the dictionary.
#         cart.append(food)                 #If it exists, the item goes into the cart list.
    
# print("----- YOUR ORDER -----") 
# for food in cart:              #Goes through each food in the cart, and Adds its price to total.
#     total += menu.get(food)    #total = total + menu.get(food)
#     print(food, end=" ")

# print()
# print(f"Total is :${total:.2f}")






###how we can generate some random numbers in Python and also create the number guessing program


# import random  #We need import because random is in a separate module, not built into Python by default.

# #random.randint()   #for random whole integer
# number = random.randint(1, 6)    #example of six-sided dice for random whole integer

# print(number)

#within the .randint method, you can place variables as well, as long as they contain numbers
# import random  

# low = 1       # variable 
# high = 100    # variable

# number = random.randint(low, high)   #so now we have place variables instead of number.

# print(number)

# #if you need a random floating number you can use the .random method
# import random  

# number = random.random()   #this will return a random floating number between 0 and 1

##in the future we will do a rock paper scissors game by using .choice method
# import random
# options = ("rock", "paper", "scissors")

# option = random.choice(options)   #We use .choice method

# print(option)

##shuffle, this time we have a deck of card, so we will use a list
# import random

# cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A",]

# random.shuffle(cards)  #we will use .shuffle method
# print(cards)  #this will show a deck of cards being shuffled already with new ordered of card




# ###Let's create number guessing game using python
# import random
# #we set the range and the answer of the guessing game
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num, highest_num)         #.randint is for random whole integer
# guesses = 0    # we need this as we need to keep track number of wrong guesses 
# is_running = True   #we want the user to keep guessing as long as our application is running

# print("Pythonn Number Guessing Game")
# print(f"Select a number between {lowest_num} and {highest_num}")

# #we need a while loop to continue the game each round
# while is_running:   #since we already make is_running a boolean variable aka. true or false (ปกติต้องเป็น while is_running == True)

#     guess = input("Enter your guess: ")

#     if guess.isdigit():  #we use if statement to make sure user put digit number only, by using .isdigit (aka if our guess is digit number (aka ตรงตามที่เราต้องการ))
#         guess = int(guess)             #if user guess digit we need to convert to a number
#         guesses += 1 #because we already make one guess

#         if guess < lowest_num or guess > highest_num:
#             print("That number is out of range")
#             print(f"Please select a number between {lowest_num} and {highest_num}")
#         elif guess < answer:          # elif means “else if” → it’s used when you want to check another condition if the previous if was false.
#             print("Too low! Try again!")
#         elif guess > answer:
#             print("Too high! Try again!")
#         else:     #because we already state all conditions to not be match with the answer, so else is left with only when user guess the correct answer
#             print(f"CORRECT! the answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False    ## to escape the while loop, as we already has correct guess that match answer,
#                                   ## we will take our boolean variable "is_running" and set that to be Falses to escape.

#     else:       #so if user guess something that is not a digit then it will show "Invalid guess" 
#         print("Invalid guess")        
#         print(f"Please select a number between {lowest_num} and {highest_num}")







# ### Rock Paper Scissors game
# import random

# options = ("rock", "paper", "scissors")
# #player = None   #we create a variable name player to store the player's choice
# #computer = random.choice(options)
# running = True  #This is to set rock paper scissors game to be able to play again if user want


# while running:   #this is equal to while running == True:  and we dont set while True: because it's hard to find where the break statement is
    
#     player = None   #we move player and computer variable down here (inside while loop) because every time we start a new game,
#     computer = random.choice(options) #we will reset the player as well as the computer, so we put inside the while loop.

#     # we need condition to limit user to only put input of rock, paper, scissors choices
#     while player not in options:  # this while loop = if the player doesn't pick one of these options, this while loop will continue forever
#         player = input("Enter a choice (rock, paper,scissors): ") #once we pick something within our options, we then escape while loop

#     print(f"Player: {player}")
#     print(f"Computer: {computer}")

#     if player == computer:
#         print("It's a tie!")
#     elif player == "rock" and computer == "scissors":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     elif player == "scissors" and computer == "paper":
#         print("You win!")
#     else:
#         print("You lose!")
    
#     if not input("Play agian? (y/n): ").lower() == "y":  #this line = if the user input, after making it lowercase, doesn't equal to y 
#         running = False                                  #for yes, it will set running to be False (aka stop running game again)

# print("Thanks for playing!")






# ###dice roller program in python
# import random

# #we need these symbol from these unic code characters to build ASI art some dices
# # print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# #● ┌ ─ ┐ │ └ ┘

# #basic box shape
# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"

# ##let's create a dictionary aka. key:value pair!!!
# dice_art = {
#     1: ("┌─────────┐",
#         "│         │",
#         "│    ●    │",
#         "│         │",
#         "└─────────┘"),
#     2: ("┌─────────┐",
#         "│  ●      │",
#         "│         │",
#         "│      ●  │",
#         "└─────────┘"),
#     3: ("┌─────────┐",
#         "│  ●      │",
#         "│    ●    │",
#         "│      ●  │",
#         "└─────────┘"),
#     4: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│         │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     5: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│    ●    │",
#         "│  ●   ●  │",
#         "└─────────┘"),
#     6: ("┌─────────┐",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "│  ●   ●  │",
#         "└─────────┘")
# } 

# dice =[]  #dice will be numbers, randomly generated between 1 and 6
# total = 0
# num_of_dice = int(input("How many dice?: "))

# for die in range(num_of_dice):
#     dice.append(random.randint(1, 6)) #We need dice.append to store each roll in the list named dice = []; otherwise only the last roll would remain.

# # for die in range(num_of_dice):
# #     for line in dice_art.get(dice[die]): #we getting value in our dictionary at the given key.
# #         print(line)

# ##to make all the dices in the horizon line display
# for line in range(5):
#     for die in dice:
#         print(dice_art.get(die)[line], end="")
#     print()

# for die in dice:
#     total += die
# print(f"total: {total}")







# function = A block of reuseable code
#            place () after the function name to invokee it

# #example: sing Happy Birth Day 3 times ปกติต้องทำยาวๆ 3รอบ
# print("Happy birthday to you!")
# print("You are old!")
# print("Happy birthday to you!")
# print()

# print("Happy birthday to you!")
# print("You are old!")
# print("Happy birthday to you!")
# print()

# print("Happy birthday to you!")
# print("You are old!")
# print("Happy birthday to you!")
# print()

## there is better way that doesn't involve repeating our code or using loops
### By writing this code once, then reuse it whenever I need to
### That's where functions come in fuctions => "def" plus fuction name and ():
# def happy_birthday():
#     print("Happy birthday to you!")
#     print("You are old!")
#     print("Happy birthday to you!")
#     print()

# #to invoke the function you type function name then add a parenthesis ()
# happy_birthday()
# happy_birthday()
# happy_birthday()

# #using argument inside the parenthesis aka("argument"), you can send values or variables directly to a function
# #BUT you need a matching set of parameters that are in order for the argument,
# def happy_birthday(name, age):             # and you can have more than 1 argument ex. name, age (the order does matter!!)
#     print(f"Happy birthday to {name}!")    #ใช้เหมือนการแทนตัวแปร with using f string and {variable/argument}
#     print(f"You are {age} years old!")
#     print("Happy birthday to you!")
#     print()

# #to invoke the function you type function name then add a parenthesis ()
# happy_birthday("Bro", 20)
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)


##this is called the positional argument
# def happy_birthday(x, y):             # the order does matter!!
#     print(f"Happy birthday to {x}!")    #ใช้เหมือนการแทนตัวแปร x,y with using f string and {variable/argument}
#     print(f"You are {y} years old!")
#     print("Happy birthday to you!")
#     print()

# #to invoke the function you type function name then add a parenthesis ()
# happy_birthday("Bro", 20)
# happy_birthday("Steve", 30)
# happy_birthday("Joe", 40)

# def display_invoice(username, amount, due_date):   # the order does matter!!
#     print(f"Hello {username}")
#     print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("Joe", 100.25, "01/02")

###explain return statement
# return = statement used to end a function
#          and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

# def create_name(first, last):  #function
#     first = first.capitalize()
#     last = last.capitalize()
#     return first + " " + last   #using return statement, you can return data back to the function

# full_name = create_name("spongebob", "squarepants")

# print(full_name)     
# #function is a section of reusable code. To use function, you type function's name, add a set of parenthesis
# #you can send some data (aka arguments) while needed matching set of parameters, you also do have option of returning data back to place in which you invoke function












# # default arguments = A default value for certain parameters default is used when that argument is omitted
# #                     make your functions more flexible, reduce # of arguments 1.positional, 2.DEFAULT, 3.keyword, 4.arbitrary

# #last topic we already dicussed positional argument, 
# #so today we gonna discuss DEFAULT argument!!!

# #Let's define function to calculate the net price, it will be 3 parameters list_price, discount, tax
# def net_price(list_price, discount, tax):
#     return list_price * (1 - discount) * (1 + tax)

# print(net_price(500, 0, 0.05))
#example, most of the time discount rate and tax rate is always the same, what we could do to make function more flexible

# #we can do it by set these two (discount, tax) parameters to have a DEFAULT value, like this below
# def net_price(list_price, discount=0, tax=0.05):    #we set discount and tax as default value
#     return list_price * (1 - discount) * (1 + tax)

# # print(net_price(500))
# # print(net_price(500 ,0.1))  # this is the case when if there is someone who has a discount
#                               # if we're passing in an argument for discount, we will use the discount that passed in rather than the default
# # if user not pay tax too 
# # print(net_price(500 ,0.1 ,0)) 

# # EXERCISE, We will create a count up timer
# import time  #import time module

# def count(start, end):
#     for x in range(start, end+1): #for loop # within the range function the second argument is exclusive, so we need to add one (+1) 
#         print(x)
#         time.sleep(1) #to make this thread that's running the program sleep
#     print("DONE!")

# count(0, 10)  #to invoke the function

# #let's assume most of the time user want to start the time at 0
# #so we gonna set 0 as default
# import time  #import time module

# def count(end, start=0):  #but remember if you use any default argument, you want to be sure that they're after any positional arguments
#     for x in range(start, end+1): 
#         print(x)
#         time.sleep(1) #to make this thread that's running the program sleep
#     print("DONE!")

# count(10)  #to invoke the function
 
# import time  #import time module

# def count(end, start=0):  #but remember if you use any default argument, you want to be sure that they're after any positional arguments
#     for x in range(start, end+1): 
#         print(x)
#         time.sleep(1) #to make this thread that's running the program sleep
#     print("DONE!")

# count(30, 15)  #to invoke the function
##so in conclusion DEFAULT argument is used when an argument are consistent most of the time







# #KEYWORD arguments = an argument preceded by an identifier helps with readability order of arguments doesn't matter
# #                      1. positional 2. default 3. KEYWORD 4. arbitrary

# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello("Hello", "Mr.", "Jayson", "Tatum")  ##right now we currently using positional argument(the order matter)

# #if we want to change position we can use keyword method for example hello("Hello", "Jayson", "Tatum", "Mr.") order มันผิดต้องแก้เป็น
# def hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# hello(first = "Jayson", last = "Tatum", title = "Mr.", greeting ="Hello")  #this is the keyword argument aka. order doesn't matter
# ##and also, if there is positional argument inside the (), make sure any positional argument are first

# #more example, print number 1 to 10 using for loop
# for x in range(1,11): #we use 11 as we want 1 to 10 because the second argument is exclusive
#     print(x, end=" ") #end=" "

# #create function to generate a phone number, but we need to pass in a country code, area code, first fews digits, last fews digits
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=1, area=123, first=456, last=7890)

# print()
# print(phone_num)


# #create function to generate a phone number, but we need to pass in a country code, area code, first fews digits, last fews digits
# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=0, area=81, first=171, last=9958)

# print()
# print(phone_num)







# # *args    = allows you to pass multiple non-key arguments
# # **kwargs = allows you to pass multiple keyword-arguments
# #            * unpacking operator
# #                      1. positional 2. default 3. keyword 4. ARBITRARY
# #ARBITRARY meaning a varying amount of arguments, as we dont know how many arguments the user is gonna pass in when they invoke function


# def add(a, b):
#     return a + b

# # print(add(1, 2))
#                         #what if we want to add 3 arguments this time
#                         # print(add(1, 2, 3)) #this cannot be worked

# #so we need to modify the function, so it can accept a varying amount of arguments in any amount
# def add(*args):    # we replace the parameters with the *args (aka arguments, *args = allows you to pass multiple non-key arguments)
#     print(type(args)) #when we use the unpacking operator, so now the argument will be packed all into a tupple
#     #we get <class 'tuple'>
# add(1, 2, 3)

# #tips: *args we can change name *args to *nums, because the name of the parameter isn't as important as the unpacking(* ดอกจัน)
# #*args → packs all inputs into a tuple
# def add(*args):    # we replace the parameters with the *args (aka arguments, *args = allows you to pass multiple non-key arguments)
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1, 2, 3, 4, 5)) #now we get result of 15

# #function to display somebody name
# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")

# display_name("Dr.", "Jayson", "Leon", "Tatum", "III")
# #you get the result as Dr. Jayson Leon Tatum III, because with the unpacking operator (* and args) we can pack all the arguments ชื่อทั้งหมด into a tupple

# #Now Let's discuss **kwargs = allows you to pass multiple keyword-arguments
# #**kwargs is keyword-arguments
# def print_address(**kwargs):
#     print(type(kwargs)) 
#     #we get <class 'dict'>
#     #so its mean we can treat kwargs as it is a dictionary

# print()
# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_address(street="123 Newtown St.", 
#               city="BKK", 
#               state="Rama3", 
#               zip="10101")


# #now we will have an excercise with both *args and **kwargs together
# #we will print shipping label
# def shipping_label(*args, **kwargs):
#     for arg in args:
#         print(arg, end=" ")
#     print()
#     for value in kwargs.values():
#         print(value, end="")

#                                     # this def shipping_label(*args, **kwargs): function is designed to accept both *args and **kwargs
# shipping_label("Dr.", "Fernando", "Torres", "III",    #this frist line is a arbitrary positional arguments
#                street="123 St mary.",                 #and the rest are arbitrary keyword arguments
#                city=" BKK",                            #
#                apt=" 100",                             #
#                state=" Duke",                          #
#                zip=" 10101")                           #









# #Iteralbes = An object/collection that can return its elements one at a time,   ######return one at a time using a loop!!!!!
# #            allowing it to be iterated over in a loop

# #Iterables is a category of returning its element one at a time

# numbers = [1, 2, 3, 4, 5]  #List [], are considered iterable, we can use them within the for loop.

# for item in reversed(numbers):  #reversed() to iterate reverse or backwards
#     print(item, end=" ")  #In short: end=" " tells "print" to finish with a space instead of starting a new line.
#                           # if we change to end="-" it will tells "print" to finish with a - instead of starting a new line

# print()
# numbers = (1, 2, 3, 4, 5)  # tupple () also iteratable

# for item in numbers: 
#     print(item)

# print()
# #Let's cover set{}
# fruits = {"apple", "orange", "banana", "coconut"} #set{} cannot be reverse

# for fruit in fruits:
#     print(fruit)

# #Let's cover string (aka character)
# name = "Jayson Tatum"

# for character in name:
#     print(character, end="")

# print()
# #lastly, dictionary is use set, and within the set{} there is a {key:value} pair(s) 
# my_dictionary = {"A": 1, "B": 2, "C": 3}
# #if you iterate over a dictionary, the dictionary gonna return all the keys but not the value
# for key in my_dictionary:
#     print(key)

# #if you need the values, we gonna follow this iterable of my dictionary, the .values() method!!
# my_dictionary = {"A": 1, "B": 2, "C": 3}

# for value in my_dictionary.values():
#     print(value)

# #if you need both keys and values, you gonna use .items() method!!
# my_dictionary = {"A": 1, "B": 2, "C": 3}

# for key, value in my_dictionary.items():
#     print(key, value)

# #we can reformat the output however we want. use the f"string"
# my_dictionary = {"A": 1, "B": 2, "C": 3}

# for key, value in my_dictionary.items():
#     print(f"{key} = {value}")











# Membership operators = used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in 

#we want to see if my letter is found in my word. (aka find in a string of a word)
word = "APPLE"

letter = input("Guess a letter in the secret word: ")
#The in membership operator will test to see if a value or a variable is found within a sequence.
if letter in word:  #"in" is going to return a boolean value of TRUE if that letter is found or FALSE if it's not
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")


#for the inverse of the in membership operator (aka not in)
#if the value or variable is not found in this sequence, it return TRUE, otherwise FALSE.
if letter not in word:  #if now it's "not in" we have to swicht/flip the statements/ที่เราพิม around, so it'll deliver same result as we want
    print(f"{letter} was not found")
else:
    print(f"There is a {letter}")

#now let's searching for a value or variable found within a set (similar to list, tuple)
#set of student
students = {"Jayson", "Fernando", "Luis"}

student = input("Enter the name of a student: ")

if student in students:
    print(f"{student} is a student")
else:
    print(f"{student} was not found")

#we can do the opposite of in (aka not in)
if student not in students:
    print(f"{student} was not found")
else:
    print(f"{student} is a student")

#now we gonna cover the dictionary
grades = {}