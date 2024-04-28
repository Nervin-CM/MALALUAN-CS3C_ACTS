print("1. Display numbers from -10 to -1 using for loop")

for num in range(-10, 0):
    print(num)


print("\n2. Use else block to display a message “Done” after successful execution of for loop")
for num in range(-10, 0):
    print(num)
else:
    print("Done", "\n")

print("\n3.Write a program to display all prime numbers within a range")
start = 2
end = 9
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            

print("\n4.Use a loop to display elements from a given list present at odd index positions")
my_list = [1, 2, 3, 4, 5, 6]
for index in range(1, len(my_list), 2):
    print(my_list[index])


print("\n5. Display numbers from a list using loop")
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num > 500:
        break
    elif num > 150:
        continue
    elif num % 5 == 0:
        print(num)



