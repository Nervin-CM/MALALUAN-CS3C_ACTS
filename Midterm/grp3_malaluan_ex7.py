#MALALUAN, NERVIN C. BSCS-3C 
#GROUP 3

import array as arr

#CREATING AND ACCESSING ARRAY ELEMENTS
# Create an array of integers
my_array = arr.array('i', [1, 3, 5])

# Access and display individual elements
print(my_array[0])  # Output: 1
print(my_array[1])  # Output: 3
print(my_array[2])  # Output: 5

#APPENDING AN ITEM
# Create an array
my_array = arr.array('i', [1, 3, 5, 7, 9])

print("\nOriginal array:", my_array, "\nAppend 11 at the end of the array:")

# Append 11 to the array
my_array.append(11)

print("New array:", my_array)

#REVERSING THE ARRAY
# Create an array
my_array = arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3])

print("\nOriginal array:", my_array)

# Reverse the array
my_array.reverse()

print("Reverse the order of the items:", my_array)


#FINDING DUPLICATE ELEMENTS
def has_duplicates(my_array):
    return len(set(my_array)) != len(my_array)

# Test cases
array1 = arr.array('i', [1, 2, 3, 4])
array2 = arr.array('i', [1, 2, 3, 2])
array3 = arr.array('i', [1, 1, 2, 3])

print("\n")
print(has_duplicates(array1))  # Output: False
print(has_duplicates(array2))  # Output: True
print(has_duplicates(array3))  # Output: True

#FINDING THE FIRST DUPLICATE ELEMENTS
def find_first_duplicate(my_array):
    seen = set()
    for num in my_array:
        if num in seen:
            return num
        seen.add(num)
    return -1

# Test cases
array1 = arr.array('i', [2, 1, 4, 4, 5])
array2 = arr.array('i', [1, 2, 3, 4])
array3 = arr.array('i', [1, 1])

print("\n")
print(find_first_duplicate(array1))  # Output: 4
print(find_first_duplicate(array2))  # Output: -1
print(find_first_duplicate(array3))  # Output: 1