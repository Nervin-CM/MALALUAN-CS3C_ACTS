#Malaluan, Nervin C. CS3C GROUP 3

#This function finds the maximum of three numbers.
def max_of_three(num1, num2, num3):
  
  return max(num1, num2, num3)

#This function sums all the numbers in a list.
def sum_of_list(numbers):
  
  return sum(numbers)

#This function reverses a string.
def reverse_string(text):
 
  return text[::-1]

#This function counts the number of upper and lower case letters in a string.
def count_upper_lower(text):
 
  upper_count = 0
  lower_count = 0
  for char in text:
    if char.isupper():
      upper_count += 1
    elif char.islower():
      lower_count += 1
  return f"Uppercase: {upper_count}, Lowercase: {lower_count}"

#This function removes duplicates from a list and returns a new list with distinct elements.
def remove_duplicates(numbers):

  return list(set(numbers))

#Output
print(max_of_three(10, 20, 5))  # Output: 20
print(sum_of_list([1, 2, 3, 4, 5]))  # Output: 15
print(reverse_string("Hello world!"))  # Output: "!dlrow olleH"
print(count_upper_lower("This is a String"))  # Output: Uppercase: 2, Lowercase: 11
print(remove_duplicates([1, 2, 2, 3, 4]))  # Output: [1, 2, 3, 4]
