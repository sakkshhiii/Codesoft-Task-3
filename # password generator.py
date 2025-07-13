# password generator

import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''
    
    all_chars = lower + upper + digits + symbols

    if not all_chars:
        return "Error: No character types selected."

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("How long should your password be? (e.g., 12): "))
        if length <= 0:
            print("Please enter a number greater than 0.")
            return

        print("\nChoose the types of characters to include:")
        use_upper = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("Include symbols (like @, #, $)? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_symbols)
        print(f"\nYour generated password is:\n{password}")
        print("Remember to save it somewhere safe.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":  
    main()
