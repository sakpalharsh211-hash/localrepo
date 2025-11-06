#Lambda function to check if a string starts with a specific character
start_with = lambda s, ch: s.startswith(ch)

#Test the lambda function
string = input("Enter a string: ")
char = input("Enter the starting character to check: ")

# check and display the result
if start_with(string, char):
    print(f"Yes, '{string} ' start with ' {char} ' . ")
else:
    print(f"No, '{string} 'does not start with ' {char} ' . ")




'''def start_with(s, ch):
    return s.startswith(ch)

# Test the function
string = input("Enter a string: ")
char = input("Enter the starting character to check: ")

if start_with(string, char):
   print(f"Yes, '{string} ' start with ' {char} ' . ")
else:
   print(f"No, '{string} 'does not start with ' {char} ' . ")'''

