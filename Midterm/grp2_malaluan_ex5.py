import math

#NUMBER FUNCTIONS
print("Number Functions")
# Absolute value
x = -5
absolute_value = abs(x)
print(absolute_value) 

# Minimum and maximum
numbers = [1, 5, 2, 8, 3]
minimum = min(numbers)
maximum = max(numbers)
print(f"Minimum: {minimum}, Maximum: {maximum}")  

# Rounding
number = 3.14159
rounded_up = round(number)
rounded_down = round(number, 0)
rounded_to_two_decimals = round(number, 2)
print(f"Rounded up: {rounded_up}, Rounded down: {rounded_down}, Rounded to two decimals: {rounded_to_two_decimals}")


#POWER AND LOGARITHMIC FUNCTIONS
# Power function
print("\nPower and Logarithmic Functions")
base = 2
exponent = 3
result = pow(base, exponent)  
print(result)  

# Logarithm with base 10
number = 100
logarithm = math.log10(number)  
print(logarithm)  

# Natural logarithm (base e)
number = 2.71828
natural_logarithm = math.log(number)  
print(natural_logarithm) 


#TRIGONOMETRIC FUNCTIONS
print("\nTrigonometric Functions")
# Sine function
angle_in_radians = math.pi / 2  # 90 degrees in radians
sine_value = math.sin(angle_in_radians)
print(sine_value)  

# Cosine function
cosine_value = math.cos(angle_in_radians)
print(cosine_value)  

# Tangent function
tangent_value = math.tan(angle_in_radians)
print(tangent_value)  


#ANGULAR CONVERSIONS FUNCTIONS
print("\nAngular Conversions Functions")
# Convert degrees to radians
degrees = 45
radians = math.radians(degrees)
print(radians)  

# Convert radians to degrees
radians = math.pi / 3
degrees = math.degrees(radians)
print(degrees)  



#HYPERBOLIC FUNCTIONS
print("\nHyperbolic Functions")
# Hyperbolic sine function
x = 1
sinh_value = math.sinh(x)
print(sinh_value)  

# Hyperbolic cosine function
cosh_value = math.cosh(x)
print(cosh_value)  

# Hyperbolic tangent function
tanh_value = math.tanh(x)
print(tanh_value)  

