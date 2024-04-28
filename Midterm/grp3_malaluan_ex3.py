# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces
var1 = "Hanni"
var2 = "Pham"
var3 = "you've worked"
var4 = "so hard"

nJ = var1 + " " + var2 + " " + var3 + " " + var4

print(nJ)

# Using + Concatenate Strings in Python get two strings from user input and concatenate them
first_str= input("Enter the first string: ")
second_str = input("Enter the second string: ")

output = first_str + " " + second_str

print(output)

# Using + Concatenate in Python using your name and your age in a paragraph
name = "Nervin Malaluan"
age = 20

output = "My name is " + name + " and I am " + str(age) + ". Always at your service."

print(output)

# Create a Python program to perform Addition Subtraction Multiplication and Division using two numbers

print("please enter a value to perform an Addition, Subtraction, Multiplication & Addition")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
multipli = num1 * num2
divide = num1 / num2
whole = num1 // num2 

print("sum: ", add)
print("difference: ", sub)
print("product: ", multipli)
print("quotient: " + str(divide) + " Without Decimal: " + str(whole))