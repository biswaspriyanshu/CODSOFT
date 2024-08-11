import random
import string

def generate_password(length):
    # Define the character sets for the password
    letters = string.ascii_letters  # Uppercase and lowercase letters
    digits = string.digits          # Digits
    punctuation = string.punctuation  # Special characters

    # Combine all character sets
    all_characters = letters + digits + punctuation

    # Generate the password using a random choice of characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    # Prompt the user to specify the length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Password length must be at least 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"Generated password: {password}")

# Run the main function
if __name__ == "__main__":
    main()
