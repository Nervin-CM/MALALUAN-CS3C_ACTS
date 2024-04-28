#MALALUAN, NERVIN C. GROUP 3 
#BSCS-3C

#Python program find difference between each number in the array and the average of all numbers
def Average(array):
    average = sum(array) / len(array)
    return [round(num - average, 2) for num in array]

array = [5, 10, 50, 90, 7]
differences = Average(array)
print(differences, "\n")

#Python program to convert a string in an array
def string_to_array(string):
  
  return list(string)


string = "Hello, world!"
array = string_to_array(string)
print(array, "\n")  

#Python program to split an array in two and store even numbers in one array and odd numbers in the other.
def split_even_odd(numbers):
  
  even_numbers = []
  odd_numbers = []
  for num in numbers:
    if num % 2 == 0:
      even_numbers.append(num)
    else:
      odd_numbers.append(num)
  return even_numbers, odd_numbers


numbers = [1, 2, 3, 4, 5]
even_numbers, odd_numbers = split_even_odd(numbers)
print("Even numbers:", even_numbers)  # Output: [2, 4]
print("Odd numbers:", odd_numbers, "\n")  # Output: [1, 3, 5]

#Python program to perform insertion sort on an array.
def insertion_sort(numbers):
  
  sorted_list = []
  for num in numbers:
    # Find the correct position for the current number in the sorted list
    i = 0
    while i < len(sorted_list) and sorted_list[i] < num:
      i += 1
    # Insert the number at the correct position
    sorted_list.insert(i, num)
  return sorted_list


numbers = [5, 2, 8, 1, 3]
sorted_numbers = insertion_sort(numbers)
print(sorted_numbers)  # Output: [1, 2, 3, 5, 8]