import string
import secrets

def generate_password():
    print("------ PASSWORD GENERATOR ------")

    length = int(input("Enter password length: "))

    print("\nChoose character sets to include:")
    include_upper = input("Include UPPERCASE letters (Y/N): ").lower() == 'y'
    include_lower = input("Include lowercase letters (Y/N): ").lower() == 'y'
    include_digits = input("Include digits (Y/N): ").lower() == 'y'
    include_symbols = input("Include symbols (Y/N): ").lower() == 'y'

    chars = ""

    if include_upper:
        chars += string.ascii_uppercase
    if include_lower:
        chars += string.ascii_lowercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No character sets selected!"

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

print("Generated Password:", generate_password())
