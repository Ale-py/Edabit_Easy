# 1. Stuttering Function
# Write a function that stutters a word as if someone is struggling to read it. The first two
#  letters are repeated twice with an ellipsis ... and space after each, and then the word is
#  pronounced with a question mark ?Assume all input is in lower case and at least two characters long.
'''
def stutter(word):
    if len(word) >= 2 and word.islower():
        first_letters = word[0:2]
        return f"{first_letters}... {first_letters}... {word}?"
    else:
        return "Assume all input is in lower case and at least two characters long."

print(stutter("outstanding"))
'''
# 2. Find the Discount
# Create a function that takes two arguments: the original price and the discount
# percentage as integers and returns the final price after the discount.
# Your answer should be rounded to two decimal places.
'''
def dis(price,discount):
    x = discount / 100
    y = x * price
    result = price - y 
    return round(result,2)

print(dis(89,20))
'''
# 3. Radians to Degrees
# Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
# The number π can be loaded from the math module with from math import pi.
'''
from math import pi

def radians_to_degrees(radians):
    rad = 180 / pi
    degrees = rad * radians
    return round(degrees,1)

print(radians_to_degrees(50))
'''
# 4. Circle or Square
# Given the radius of a circle and the area of a square, return True if the circumference of the
# circle is greater than the square's perimeter and False if the square's perimeter is greater
# than the circumference of the circle.You can use Pi to 2 decimal places (3.14).
# Circumference of a circle equals 2 * Pi * radius.
# To find the perimeter of a square using its area, find the square root of area (to get side length) and multiply that by 4.
'''
import math 
from math import pi

def circle_or_square(radius,area):
    circumference = 2 * round(pi,2) * radius
    perimeter = math.sqrt(area) * 4
    if circumference > perimeter:
        return True
    else:
        return False

print(circle_or_square(16,625))   
'''
# 5. Curzon Numbers
# In this challenge, establish if a given integer num is a Curzon number. If 1 plus 2 elevated to
# num is exactly divisible by 1 plus 2 multiplied by num, then num is a Curzon number.
# Given a non-negative integer num, implement a function that returns True if num is a Curzon number, or False otherwise.
'''
def is_curzon(num):
    if num > 0:
        x = 2 ** num + 1
        y = 2 * num + 1
        if x % y == 0:
            return True
        else:
            return False
    else:
        return "Give a non-negative integer"
print(is_curzon(14))
'''
# 6. Luke, I Am Your ...
# Luke Skywalker has family and friends. Help him remind them who is who. Given a string
# with a name, return the relation of that person to Luke.
# Darth Vader-father,Leia-sister,Han-brother in law,R2D2-droid
'''
person_relation = {
    "Darth Vader" : "father",
    "Leia" : "sister",
    "Han" : "brother in law",
    "R2D2" : "droid"
}

def relation_to_luke(name):
    
    if name in person_relation:
        return f"Luke, I am your {person_relation[name]}"
    else:
        return "Person does not exist"

print(relation_to_luke("R2D2"))
'''
# 7. Sum of Resistance in Series Circuits
# When resistors are connected together in series, the same current passes through each
# resistor in the chain and the total resistance, RT, of the circuit must be equal to the sum of
# all the individual resistors added together. That is: RT = R1 + R2 + R3 ...
# Create a function that takes an array of values resistance that are connected in series, and
# calculates the total resistance of the circuit in ohms. The ohm is the standard unit of
# electrical resistance in the International System of Units ( SI ).
# All inputs will be valid.Notice the singular ohm for values <= 1.
'''
def series_resistance(array_of_values):
    total_resistance = sum(array_of_values)
    if total_resistance <= 1:
        return f"\"{total_resistance} ohm\""
    else:
        return f"\"{total_resistance} ohms\""

print(series_resistance([1,5,6,3]))
'''
# 8. Solving Exponential Equations With Logarithms
# Create a function that takes a number a and finds the missing exponent x so that a when raised to the power of x is equal to b.
'''
import math

def solve_for_exp(x,base):
    exponent = math.log(base,x)
    return round(exponent)

print(solve_for_exp(9,3486784401))
'''
# 9. Invert Colors
# Create a function that inverts the rgb values of a given tuple.
# Must return a tuple.
'''
def color_invert(rgb):
    mytuple = rgb
    r = 255 - mytuple[0]
    g = 255 - mytuple[1]
    b = 255 - mytuple[2]
    list1 = [r,g,b] 
    mytuple = tuple(list1)

    return mytuple
print(color_invert((255, 255, 255)))
'''
# 10. End Corona!
# Create a function that takes the number of daily average recovered cases recovers, daily
# average new_cases, current active_cases, and returns the number of days it will take to
# reach zero cases.The number of people who recover per day recovers will always be greater than daily new_cases.
# Be conservative and round up the number of days needed.
'''
import math
def end_corona(recovers,new_cases,active_cases):
    while recovers > new_cases:
        number_of_days = active_cases / (recovers - new_cases)
        return math.ceil(number_of_days)
    else:
        return "The number of people who recover per day will always be greater than new cases"

print(end_corona(1000,2000,77000))
'''

