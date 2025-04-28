def is_armstrong_number(num):
    # Convert the number to a string to easily iterate over digits
    num_str = str(num)
    # Calculate the number of digits (which is 4 for a 4-digit number)
    num_digits = len(num_str)
    # Initialize the sum
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Example usage
num = 1634
if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
