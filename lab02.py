import math

first_name = "Sylvan"
name = first_name
last_name = "Coleman"
full_name = first_name + " " + last_name
age = 21
height = 5.2
favorite_color = "Mint"

print(name)
print(age)
print(height)
print(favorite_color)

print(name,age,height,favorite_color)
print(f"Hello: {full_name} my favorite color is: {favorite_color}")
print(f"{name}'s age is {age} years old")
print(f"{name}'s height is {height} feet")

print(f"""
Name: {full_name}
Age: {age} years old
Height: {height} feet
Favorite Color: {favorite_color}
""")

# Part Two

circle_area = 5*3.14159
age_math = math.sqrt(age)
height_math1 = math.sin(height)
height_math2 = math.cos(height)
print(circle_area, age_math, height_math1, height_math2)

# Part Three

mvar1 = (age + 5)
mvar2 = (height-4)
mvar3 = (age * height)
mvar4 = (height/2)
mvar5 = (age%3)
mvar6 = (age**2)
print(f"{age} + 5 = {mvar1} \n{height} - 4 = {mvar2} \n{age} * {height} = {mvar3}, "
      f"{height}/2 = {mvar4}\nThe remainder of {age}/3 is {mvar5}\n{age} to the power of 2 is {mvar6}\n")

# Part Four

# Celsius = (Fahrenheit - 32) * (5/9)

an_input  = int(input("Enter a degree in Celsius to be converted into Fahrenheit\n"))
to_fahrenheit = ((an_input - 32)*(5/9))
print(f"{an_input}\N{DEGREE SIGN} Celsius is {to_fahrenheit}\N{DEGREE SIGN} Fahrenheit\n")