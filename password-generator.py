import random
import string

def generate_password(length=12, use_numbers=True, use_special_characters=True):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special_characters:
        characters += string.punctuation

    if length < 4:
        return "Password length must be at least 4 character."
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length = int(input("Enter the desired password length: "))
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_characters = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_numbers, use_special_characters)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
