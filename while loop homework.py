# Backward counting program using while loop

# Get input from the user
number = input("Enter a number to count backward from: ")

# Check if the input is a valid number
if number.isdigit():
    number = int(number)
    print(f"Counting backward from {number} to 0:")
    while number >= 0:
        print(number)
        number -= 1
else:
    print("Please enter a valid positive integer.")