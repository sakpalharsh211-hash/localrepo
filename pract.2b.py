number = input("Enter a number: ")
n = int(number)

# Initialize sum
sum_of_digit = 0

while n > 0:
    sum_of_digit += n % 10  # extract last digit
    n //= 10                # remove last digit

print("Sum of digits:", sum_of_digit)
