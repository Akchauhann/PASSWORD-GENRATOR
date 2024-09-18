import random
import string

def generate_password(length):
    # Define characters to use in password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choices
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    # Ask user for the password length
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if length < 1:
                print("Please enter a valid length (greater than 0).")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
