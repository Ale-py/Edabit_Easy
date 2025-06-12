# 11. Basic Calculator
# Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.
# If the input tries to divide by 0, return: "Can't divide by 0!"
'''
def calculator(num1,operator,num2):
    if num2 == 0:
        return  "Can't divide by 0!"
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    else:
        return num1 / num2
    
print(calculator(0,"/",3))
'''
# 12. Calculating Damage
# Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
# Return "invalid" if damage or speed is negative.
'''
def damage(dmg,speed,time):
    total = 0
    while dmg > 0 and speed > 0:
        if time == "second":
            total = dmg * speed
        elif time == "minute":
            total = dmg * speed * 60
        else:
            total = dmg * speed * 3600
        return total
    else:
        return "invalid"

print(damage(2, 0, "hour"))
'''
# 13. Let's Sort This List!
# Create a function that takes a list of numbers lst, a string s and return a list of numbers as per the following rules:
# "Asc" returns a sorted list in ascending order.
# "Des" returns a sorted list in descending order.
# "None" returns a list without any modification.
'''
def asc_des_none(nums,order):
    numbers_list = nums
    if order == "Asc":
        numbers_list.sort()
    elif order == "Des":
        numbers_list.sort(reverse=True)
    else:
        return numbers_list
    return numbers_list

print(asc_des_none([1, 2, 3, 4], "None"))
'''
# 14. Return the Factorial
# Create a function that takes an integer and returns the factorial of that integer. That is, the integer multiplied by all positive lower integers.
# Assume all inputs are greater than or equal to 0.
'''
def factorial(num):
    total = 1
    for x in range(1,num+1):
        total = total * x
    return total

print(factorial(13))
'''
'''
import math
print(f"The factorial of 23 is : {math.factorial(23)}")
'''
# 15. Number Split
# Given a number, return a list containing the two halves of the number. If the number is odd, make the rightmost number higher.
# All numbers will be integers.You can expect negative numbers too.
'''
import math

def number_split(num):
    x = num / 2
    num_list = []

    if num % 2 == 0:
        num_list.append(int(x))
        num_list.append(int(x))
        return num_list
    else:
        num_list.append(math.floor(x))
        num_list.append(math.ceil(x))
        return num_list

print(number_split(-9))
'''


#✅






























