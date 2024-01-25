# Write a program to iterate the first 10 numbers, 
# and in each iteration, print the sum of the current and previous number.

# Set a starting variable of 0

previous_number = 0

# Make iteration, range of 10
# Print the sum of current and previous number

for i in range(1, 11):
    sum_of_current_and_previous = previous_number + i
    print("Current Number", i, "Previous Number", previous_number, "Sum", sum_of_current_and_previous)
    previous_number = i