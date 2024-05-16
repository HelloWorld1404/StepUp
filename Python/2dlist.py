#!/usr/bin/env python
# coding: utf-8

# ## print("Hello")

# In[ ]:


def calculate_pizza_cost(size, toppings):
    base_prices = {"Small": 10, "Medium": 15, "Large": 20}
    topping_cost = 2
    total_cost = base_prices[size] + (toppings * topping_cost)
    return total_cost
size = input()
toppings = int(input())
total_cost = calculate_pizza_cost(size, toppings)

print(size)
print(toppings)
print(f"${total_cost}")
print("Thank you for ordering from PizzaHut!")


# In[ ]:


def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

num = int(input())
factorial_result = calculate_factorial(num)

print(f"{factorial_result}")


# In[ ]:


print("Leap Year Checker")
print("------------------")

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("{} is a leap year.".format(year))
else:
    print("{} is not a leap year.".format(year))


# In[ ]:


print("GPA Calculator")
print("--------------")

num_courses = int(input("Enter the number of courses: "))
total_credit_hours = 0
total_grade_points = 0

for i in range(1, num_courses + 1):
    print("\nCourse", i, ":")
    grade = input("Grade (A, B, C, D, F): ")
    credit_hours = int(input("Credit Hours: "))
    
    if grade == 'A':
        grade_points = 4.0
    elif grade == 'B':
        grade_points = 3.0
    elif grade == 'C':
        grade_points = 2.0
    elif grade == 'D':
        grade_points = 1.0
    else:
        grade_points = 0.0
    
    total_credit_hours += credit_hours
    total_grade_points += grade_points * credit_hours

if total_credit_hours != 0:
    gpa = total_grade_points / total_credit_hours
    print("\nCalculated GPA:", round(gpa, 2))
else:
    print("\nNo courses entered.")


# In[ ]:


print("Countdown Timer")
print("----------------")

countdown_duration = int(input("Enter the countdown duration (in seconds): "))

while countdown_duration > 0:
    print("{} seconds remaining...".format(countdown_duration))
    countdown_duration -= 1

print("Time's up!")


# In[ ]:


print("Number Summation")
print("----------------")

n = int(input("Enter a positive integer: "))
sum = 0
current_number = 1

while current_number <= n:
    sum += current_number
    current_number += 1

print("\nSum of numbers from 1 to {}: {}".format(n, sum))


# In[ ]:


print("Number Summation")
print("----------------")

n = int(input("Enter a positive integer: "))
sum = 0
while n >= 1:
    sum += n
    n -= 1

print("\nSum of numbers from 1 to {}: {}".format(n, sum))


# In[ ]:


temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C/F): ")

if unit.lower() == 'c':
    converted_temperature = (temperature * 9/5) + 32
    converted_unit = 'Fahrenheit'
elif unit.lower() == 'f':
    converted_temperature = (temperature - 32) * 5/9
    converted_unit = 'Celsius'
else:
    print("Invalid unit entered.")
    exit()

print("\nConverted temperature: {:.2f} {}".format(converted_temperature, converted_unit))




# In[ ]:


n = int(input("Enter a positive integer: "))
sum = 0
current_number = 1

while current_number <= n:
    sum += current_number
    current_number += 1

print("\nSum of numbers from 1 to {}: {}".format(n, sum))


# In[ ]:


n = int(input("Enter a positive integer: "))
sum = 0
while n<10:
    sum= sum+n
    n +=1

print(sum)


# In[ ]:


import random
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

secret_number = random.randint(min_value, max_value)

print("\nWelcome to NumberGuess! Try to guess the secret number.")
print("Guess a number between {} and {}:".format(min_value, max_value))

while True:
    guess = int(input())
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the number {}.".format(secret_number))
        break


# In[ ]:


# Initialize the account balance
account_balance = 1000  # You can set an initial balance of your choice

# Function to display the ATM menu
def display_menu():
    print("\nWelcome to Simple ATM")
    print("1. Check Balance")
    print("2. Deposit Funds")
    print("3. Withdraw Funds")
    print("4. Exit")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(f"Your account balance is: ${account_balance}")
    elif choice == '2':
        deposit_amount = float(input("Enter the amount you want to deposit: $"))
        if deposit_amount > 0:
            account_balance += deposit_amount
            print(f"Deposit of ${deposit_amount} was successful.")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")
    elif choice == '3':
        withdraw_amount = float(input("Enter the amount you want to withdraw: $"))
        if withdraw_amount > 0 and withdraw_amount <= account_balance:
            account_balance -= withdraw_amount
            print(f"Withdrawal of ${withdraw_amount} was successful.")
        elif withdraw_amount > account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")
    elif choice == '4':
        print("Thank you for using Simple ATM. Have a nice day!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4).")


# In[ ]:


# Define the range boundaries
start_range = 10
end_range = 30

# Iterate through the range and print odd numbers
print(f"All odd numbers between {start_range} and {end_range}:")
for number in range(start_range, end_range + 1):
    if number % 2 != 0:  # Check if the number is odd
        print(number)


# In[5]:


# Print the sum of even numbers of a list
# Define a list of numbers
numbers = [1, 2, 3, 4, 5, 6]

# Initialize a variable to store the sum of even numbers
even_sum = 0

# Iterate through the list of numbers using a for loop
for num in numbers:
    # Check if the current number is even
    if num % 2 == 0:
        # If it's even, add it to the sum
        even_sum += num

# Print the sum of even numbers
print("Sum of even numbers:", even_sum)  # Output will be 12


# In[6]:


#Number guessing using for loop
import random

print("Number Guessing Game")
print("---------------------")
print("Welcome to NumberGuess! Try to guess the secret number.")

# Get the minimum and maximum values for the range
min_value = int(input("Enter the minimum value: "))
max_value = int(input("Enter the maximum value: "))

# Generate a random number between min_value and max_value
secret_number = random.randint(min_value, max_value)

for attempt in range(1, 6):  # Allow the player 5 attempts
    guess = int(input(f"Guess a number between {min_value} and {max_value}: "))
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number}.")
        break
else:
    print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")


# ##### write a Python program to count the number of vowels
# input_string = input("Enter a string: ")
# vowel_count = 0
# 
# for char in input_string:
#     if char.lower() in 'aeiou':
#         vowel_count += 1
# 
# print(f"The number of vowels in the string is: {vowel_count}")
# 

# In[ ]:


#Printing Multiples

num = int(input("Enter an integer: "))
print("Multiples of", num, ":")
for i in range(1, 11):
    print(num * i)


# In[ ]:


input_string = input("Enter a string: ")
vowel_count = 0

for char in input_string:
    if (char=='a' or char=='A' or char=='e' or char=='E' or char=='i' or char=='I' or char=='o' or char=='O' or char=='u' or char=='U'):
        vowel_count += 1
        print(char)

print(f"The number of vowels in the string is: {vowel_count}")


# In[1]:


n=int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end= " ")
    print()


# In[ ]:





# In[ ]:


n=int(input())
i=1
sum=0
while i<=n:
    if i%2==0:
        sum +=i
    i +=1
print(sum)


# In[ ]:


n = int(input())

for n in range(1, n+1):

    for m in range(1, n+1):

        print(m, end=" ")

    print("")


# In[ ]:


n = int(input())

digit = n

for k in range(n, 0, -1):

    for m in range(0, k):

        print(digit, end=' ')

    print(" ")


# In[ ]:


n = int(input())

for i in range(n):

    for k in range(i):

        print(i, end=" ")

    print(" ")


# In[ ]:


n = 7

m = 0

for k in range(n, 0, -1):

    m += 1

    for n in range(1, k + 1):

        print(m, end=' ')

    print('\r')


# In[ ]:


n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if j==1 or j==i:
            print("1",end='')
        else:
            print(i-1,end='')
        j=j+1
    print()
    i=i+1


# In[2]:


n = int(input())
i = 1

while i <= n:
    for s in range(n, i, -1):
        print(" ", end="")

    j = 1
    while j <= i:
        if j == 1 or j == i:
            print("1", end=" ")
        else:
            print(i - 1, end=" ")
        j = j + 1

    print()
    i = i + 1


# In[3]:


n = int(input())

# Outer loop for each row
for i in range(1, n + 1):
    # Print leading spaces
    for space in range(n, i, -1):
        print(" ", end="")

    # Initialize the value to be printed
    value = 1

    # Inner loop for each element in the row
    for j in range(1, i + 1):
        # Print the current value
        print(value, end=" ")

        # Update the value for the next element
        if j < i:
            value = i

    # Move to the next line for the next row
    print()


# In[4]:


n = int(input())

# Outer loop for each row
for i in range(1, n + 1):
    # Print leading spaces
    for space in range(n, i, -1):
        print(" ", end="")

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("1", end="")
        else:
            print(i - 1, end="")

    print()


# In[ ]:


curr = 1

end = 2

n = 4

for k in range(n):

    for m in range(1, end):

        print(curr, end=' ')

        curr += 1

    print("")

    end += 2


# In[ ]:


#Function
def even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
even(5)


# In[ ]:


def sum(a,b):
    return a+b
sum(5,6)


# In[ ]:


def funtion(a,b):
    if a>b:
        print("A is greater")
    else: 
        print("B is greater")
funtion(5,6)


# In[ ]:


def funtion(a,b,c):
    if a>b and a>c:
        print("A is greater")
    elif b>a and b>c: 
        print("B is greater")
    else:
        print("C s greater")
funtion(8,6,7)


# In[ ]:


list=[4,6,7,3,9,10]
def function(list):
    print(max(list))
function(list)


# In[ ]:


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum((8, 2, 3, 0, 7)))


# In[ ]:


def test_range(n):
    if n in range(3,9):
        print( " %s is in the range" %str(n))
    else :
        print("The number is outside the given range.")
test_range(5)


# In[ ]:





# In[ ]:


n = 7

m = 0

for row in range(n, 0, -1):

    m += 1

    for n in range(1, k + 1):

        print("*", end=' ')

    print('\r')


# In[ ]:


n = 7

for row in range(n, 0, -1):
    print("* " * row)


# In[ ]:


import string

def print_alphabet():
    for letter in string.ascii_uppercase:
        print(letter, end=' ')

print_alphabet()


# In[ ]:


n=int(input())
for row in range(n,0,-1):
    for column in range(1,row+1):
        print(row, end= "")
    print()


# In[ ]:


n = int(input())
for row in range(n, 0, -1):
    for num in range(1, row + 1):
        print(row, end=' ')
    print()


# In[ ]:


n = 7
m = 0
for k in range(n, 0, -1):

    m += 1

    for n in range(1, k + 1):

        print(m, end=' ')

    print('\r')


# In[ ]:


n = 7

for m in range(1, n + 1):
    for c in range(m):
        print(m, end=' ')
    print()


# In[ ]:


n = 7  # Number of rows

for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(i, end=' ')
    print()


# In[ ]:


# Function and its related problem statements
# Q.1 
'''Create a Python program that takes two numbers 
and an arithmetic operation (addition, subtraction, multiplication, division) as input 
from the user and then calls the corresponding function to perform the operation and display the result.
'''

# Define functions for each arithmetic operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed."
    return x / y

# Get user input for numbers and operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the arithmetic operation (+, -, *, /): ")

# Perform the operation based on user input
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)
else:
    result = "Invalid operation"

# Display the result
print("Result:", result)


# In[ ]:


'''Q2. Write a function that calculates the factorial of a given integer. 
Test the function with various inputs, including edge cases
'''
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test the function with various inputs
for num in range(0, 11):
    print(f"Factorial of {num} is {factorial_iterative(num)}")


# In[3]:


'''Create a function that checks whether a given string is a palindrome or not 
(reads the same forwards and backwards).'''

def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for a case-insensitive check
    clean_string = input_string.replace(" ", "").lower()
    
    # Compare the cleaned string with its reverse
    return clean_string == clean_string[::-1]

# Test the function with various inputs
test_strings = ["racecar", "hello", "A man a plan a canal Panama", "Was it a car or a cat I saw", "Madam In Eden, I'm Adam"]

for test_str in test_strings:
    result = is_palindrome(test_str)
    if result:
        print(f"'{test_str}' is a palindrome.")
    else:
        print(f"'{test_str}' is not a palindrome.")


# In[13]:


'''Write a function that counts the number of words in a given text string. 
Test it with different sentences and paragraphs.
'''
def count_words(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    
    # Count the number of words in the list
    return len(words)

# Test the function with different sentences and paragraphs
text1 = "This is a simple sentence."
text2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
text3 = """
Python is a high-level programming language that is known for its simplicity and readability.
It is widely used in web development, data analysis, and artificial intelligence.
"""

# Count words in the test strings
word_count1 = count_words(text1)
word_count2 = count_words(text2)
word_count3 = count_words(text3)

# Display the word counts
print(f"Word count in text1: {word_count1}")
print(f"Word count in text2: {word_count2}")
print(f"Word count in text3: {word_count3}")


# In[ ]:


'''Create a function that converts temperatures between Celsius and
Fahrenheit and allows the user to choose the conversion direction.'''

def convert_temperature():
    print("Temperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Enter your choice (1/2): ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid choice")

# Call the function to convert temperatures
convert_temperature()


# In[ ]:


'''Create a function that takes a person's height and
weight as input and returns their Body Mass Index (BMI).'''

def calculate_bmi(height, weight):
    # Convert height from centimeters to meters
    height_meters = height / 100
    
    # Calculate BMI
    bmi = weight / (height_meters ** 2)
    
    return bmi

# Get user input for height and weight
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

# Calculate and display BMI
bmi = calculate_bmi(height, weight)
print(f"Your BMI is: {bmi:.2f}")


# In[ ]:


'''Design a function that generates a random password of a specified length with a mix 
of uppercase letters, lowercase letters, numbers, and special characters.'''

import random
import string

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Specify the desired password length
password_length = int(input("Enter the desired password length: "))

password = generate_random_password(password_length)
print("Generated Password:", password)


# In[ ]:


'''
At "PizzaHut," customers can order pizzas with various toppings. The price of each pizza is determined by its size and the number of toppings. Write a Python program that helps calculate the total cost of a pizza order.

Your program should implement the following:

Define a function called calculate_pizza_cost that takes two arguments:

size: The size of the pizza ("small," "medium," or "large").
toppings: The number of toppings the customer wants on the pizza (an integer).

Inside the function, set the base price for each pizza size:

Small: $10
Medium: $15
Large: $20

Calculate the total cost by adding the base price and the cost of toppings. Each topping costs $2.

Display the size of the pizza, the number of toppings, the total cost, and a thank you message.


Sample Input:
Large
0
Sample Output:
Large
0
$20
Thank you for ordering from PizzaHut!  



'''

def calculate_pizza_cost(size, toppings):
    # Define base prices for each pizza size
    base_prices = {"small": 10, "medium": 15, "large": 20}
    
    # Check if the specified size is valid
    if size.lower() not in base_prices:
        return "Invalid pizza size. Please choose 'small,' 'medium,' or 'large.'"
    
    # Calculate the total cost
    base_price = base_prices[size.lower()]
    toppings_cost = toppings * 2
    total_cost = base_price + toppings_cost
    
    # Display the order details
    print("Pizza Size:", size.capitalize())
    print("Number of Toppings:", toppings)
    print("Total Cost: $", total_cost)
    print("Thank you for your order!")

# Get user input for pizza size and toppings
size = input("Enter the pizza size (small, medium, or large): ")
toppings = int(input("Enter the number of toppings: "))

# Calculate and display the total cost
result = calculate_pizza_cost(size, toppings)
if isinstance(result, str):
    print(result)


# In[ ]:


'''
"MathWiz" Academy is teaching its students about the concept of recursion. To practice this concept, 
they have assigned a problem related to calculating the factorial of a given positive integer using recursion.

Write a Python program that accomplishes the following:

Define a recursive function named calculate_factorial that takes an integer n as an argument.

Inside the function:

Base case: If n is 0 or 1, return 1.
Recursive case: Return n multiplied by the result of calling calculate_factorial with n-1.

Input a positive integer num from the user.

Call the calculate_factorial function with num as an argument and display the result.

Your program should compute the factorial of a number using recursion.


'''
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

num = int(input())
factorial_result = calculate_factorial(num)

print(f"{factorial_result}")


# In[15]:


'''
Write a program with a function that accepts a string from keyboard and create a 
new string after converting character of 
each word capitalized. For instance, 
if the sentence is “stop and smell the roses” the output should be “Stop And Smell The Roses”
'''

def capital(sentence):
    words = sentence.split() 
    capital_sentence = [word.capitalize() for word in words]  
    return ' '.join(capital_sentence)  


sentence = input("Enter a sentence: ")


result = capital(sentence)
print("Capitalized Sentence:", result)


# In[ ]:


'''
Write a program that accepts a list from user. 
Your program should reverse the content of list and display it. 
Do not use reverse () method.
'''
def reverse_list(input_list):
    reversed_list = []
    for item in input_list[::-1]:
        reversed_list.append(item)
    return reversed_list

# Get a list from the user
user_input = input("Enter a list of elements separated by spaces: ")
user_list = user_input.split()  # Split the input string into a list of elements

# Reverse the list
reversed_result = reverse_list(user_list)

# Display the reversed list
print("Reversed List:", reversed_result)




# In[ ]:





# In[2]:


# Get a list from the user
user_list = input("Enter a list of elements separated by spaces: ").split()

# Reverse the list in-place using the reverse() method
user_list.reverse()

# Display the reversed list
print("Reversed List:", user_list)


# In[11]:


n= int(input())
for row in range(1,n+1):
    for column in range(1, row+1):
        print(row, end= " ")
    print()


# In[12]:


n= int(input())
for row in range(n,0,-1):
    for column in range(1, row+1):
        print("*", end= " ")
    print()


# In[ ]:





# In[ ]:





# In[ ]:





# In[4]:


word=input()
a=len(word)
print(a)


# In[5]:


#count lenght of a word using function
word=input()
def fun(word):
    return len(word)
fun(word)


# In[3]:


#count the words on a sentence
word=input()
def fun(word):
    a=word.split()
    return len(a)
print(fun(word))


# In[2]:


#factorial of a number with recursion
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = int(input())
result = fact(num)

print(f"{result}")


# In[ ]:





# In[1]:





# In[6]:


#Function to Check palindrome
word=input()
def is_palindrome(word):
    a = word.replace(" ", "").lower()
    return a == a[::-1]
result = is_palindrome(word)
if result:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")


# In[7]:


''' Write a recursive function to calculate the nth term of the Fibonacci sequence. 
The Fibonacci sequence is a series of numbers where each term is the sum of the
two preceding ones, starting from 0 and 1. Mathematically, it's defined as:'''


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(5))  # Output: 5
print(fibonacci(10)) # Output: 55


# In[9]:


'''Write a recursive function that calculates the sum of digits of a positive integer. 
For example, the sum of digits of 12345 should be 15.'''

def sum(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum(n // 10)

print(sum(12345))


# In[1]:


'''Greatest Common Divisor (GCD)
Write a recursive function to find the greatest common divisor (GCD) of two positive integers a and b.'''
a=int(input())
b=int(input())
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(a,b))


# In[1]:


#Calling a funcion within other functiondef A():
    print('A')
    B()
    print('B')
def B():
    print('B')
    a= fact(4)
    print(a)
    print('C')
def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))
A()


# In[1]:


# Creating a 3x3 2D list filled with zeros
matrix = [[0 for _ in range(3)] for _ in range(3)]
print(matrix)


# In[2]:


N = 5
ar = [0]*N
print(ar)


# In[3]:


N = 5
arr = [0 for i in range(N)]
print(arr)


# In[4]:


rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)


# In[5]:


rows, cols = (5, 5)
arr = [[1]*cols]*rows
print(arr, "before")

arr[0][0] = 2 # update only one element
print(arr, "after")


# In[6]:


# Creating 2D List using List Comprehension
rows, cols = (5, 5)
arr = [[2 for i in range(cols)] for j in range(rows)]
print(arr)


# In[7]:


#Initializing 2D Array

rows, cols = (5, 5)

# method 1 1st approach

arr = [[0]*cols]*rows

# lets change the first element of the
# first row to 1 and print the array

arr[0][0] = 1

for row in arr:
    print(row)

# method 1 2nd approach
arr = [[0 for i in range(cols)] for j in range(rows)]

# again in this new array lets change
# the first element of the first row
# to 1 and print the array
arr[0][0] = 1
for row in arr:
	print(row)


# In[8]:


# Create a 2D list representing a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in the 2D list
print("Element at row 1, column 2:", matrix[0][1])  # Output: 2
print("Element at row 3, column 1:", matrix[2][0])  # Output: 7

# Iterating through the 2D list
print("Iterating through the matrix:")
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()


# In[9]:


# Modifying elements in the 2D list
matrix[1][1] = 99
print("Updated matrix:")
for row in matrix:
    print(row)


# In[10]:


def transpose_matrix(matrix):
    # Determine the number of rows and columns in the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix with dimensions swapped (transpose)
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    # Populate the transposed matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


# In[11]:


'''
You are given a 2D matrix represented as a list of lists. Your task is to write a Python function 
transpose_matrix(matrix) that takes this matrix as input and returns its transpose.

Input:

A 2D matrix represented as a list of lists.
Output:

The transpose of the input matrix.

'''

def transpose_matrix(matrix):
    # Determine the number of rows and columns in the input matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix with dimensions swapped (transpose)
    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    # Populate the transposed matrix
    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose_matrix(matrix)
print("Input Matrix:")
for row in matrix:
    print(row)
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)


# In[12]:


'''
Find the Maximum Element in a 2D List

Description:

You are given a 2D list representing a grid of numbers. Your task is to write a 
Python function find_max_element(matrix) that takes this matrix as input and returns the maximum element 
present in the entire matrix.

Input:

A 2D matrix represented as a list of lists.
Output:

The maximum element in the matrix.

# Input matrix
matrix = [
    [12, 34, 45, 56],
    [7, 8, 9, 10],
    [23, 67, 2, 9]
]

# Output (maximum element)
max_element = find_max_element(matrix)


# In[13]:


'''
Find the Maximum Element in a 2D List

Description:

You are given a 2D list representing a grid of numbers. Your task is to write a 
Python function find_max_element(matrix) that takes this matrix as input and returns the maximum element 
present in the entire matrix.

Input:

A 2D matrix represented as a list of lists.
Output:

The maximum element in the matrix.

# Input matrix
matrix = [
    [12, 34, 45, 56],
    [7, 8, 9, 10],
    [23, 67, 2, 9]
]

# Output (maximum element)
max_element = find_max_element(matrix)

Output:
max_element = 67


# In[14]:


def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition")

    # Get the dimensions of the matrices
    num_rows = len(matrix1)
    num_cols = len(matrix1[0])

    # Initialize a new matrix for the result
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Perform matrix addition
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix


# In[15]:


# Adding two matrices of the same size
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print(result)


# In[16]:


# Transposing a matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

transpose_matrix = [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        transpose_matrix[j][i] = matrix[i][j]

print(transpose_matrix)



# In[17]:


# Finding the maximum element in a matrix
matrix = [[1, 2, 3],
          [4, 9, 6],
          [7, 8, 5]]

max_element = matrix[0][0]
for row in matrix:
    for element in row:
        if element > max_element:
            max_element = element

print("Maximum Element in the Matrix:", max_element)


# In[18]:


# Checking if a matrix is symmetric
matrix = [[1, 2, 3],
          [2, 4, 5],
          [3, 5, 6]]

is_symmetric = True
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

if is_symmetric:
    print("The matrix is symmetric.")
else:
    print("The matrix is not symmetric.")


# In[19]:


def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions for addition")

    # Get the dimensions of the matrices
    num_rows = len(matrix1)
    num_cols = len(matrix1[0])

    # Initialize a new matrix for the result
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Perform matrix addition
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

    return result_matrix

# Example usage:
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result_matrix = matrix_addition(matrix1, matrix2)
for row in result_matrix:
    print(row)