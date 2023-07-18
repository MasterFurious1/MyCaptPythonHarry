def most_frequent(input_string):
    # Create an empty dictionary to store the letter frequency
    frequency_dict = {}

    # Count the frequency of each letter in the input_string
    for char in input_string:
        if char.isalpha():  # Ignore non-alphabetic characters
            char = char.lower()  # Convert to lowercase to count letters case-insensitively
            frequency_dict[char] = frequency_dict.get(char, 0) + 1

    # Sort the letters by their frequency in decreasing order
    sorted_letters = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)

    # Print the letters and their frequencies
    for letter, frequency in sorted_letters:
        print(f"{letter} = {frequency:02d}", end=" ")

# Input string from the user
input_string = input("Please enter a string: ")

most_frequent(input_string)
