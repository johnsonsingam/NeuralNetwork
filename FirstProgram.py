#Question 1.

def fullname(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name

def string_alternative(input_str):
    return input_str[::2]

def main():
    # Get user input
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Call the fullname function
    full_name = fullname(first_name, last_name)

    # Call the string_alternative function
    result = string_alternative(full_name)

    # Display the result
    print("Full Name:", full_name)
    print("Output:", result)

# Call the main function
if __name__ == "__main__":
    main()
