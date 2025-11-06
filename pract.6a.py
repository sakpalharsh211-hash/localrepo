# Accept input string from the user
text = input("Enter a string: ")

# count characters (excluding leading/trailing space)
num_characters = len(text)

# split the string into words
words = text.split()

# count word
num_words = len(words)

# Display the results
print("Number of characters :", num_characters)
print("Number of words:", num_words)
