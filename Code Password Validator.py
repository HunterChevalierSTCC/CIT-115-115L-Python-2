def main():
    sName = input("Enter full name such as John Smith: ")
    sInitials = get_initials(sName)

    while True:
        sPassword = input("Enter new password: ")

        if validate_password(sPassword, sInitials):
            print("Password is valid and OK to use.")
            break


def get_initials(name):
    names = name.split()
    return (names[0][0] + names[-1][0]).upper()


def validate_password(password, initials):
    is_valid = True
    errors = []

    if len(password) < 8 or len(password) > 12:
        errors.append("Password must be between 8 and 12 characters")
        is_valid = False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^"

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_lower:
        errors.append("Password must contain at least 1 lowercase letter")
        is_valid = False

    if not has_upper:
        errors.append("Password must contain at least 1 uppercase letter")
        is_valid = False

    if not has_special:
        errors.append("Password must contain at least 1 of these special characters: !@#$%^")
        is_valid = False

    if initials.lower() in password.lower():
        errors.append("Password must not contain user initials.")
        is_valid = False

    if password.lower().startswith("pass"):
        errors.append("Password can't start with Pass.")
        is_valid = False

    if not has_digit:
        errors.append("Password must contain at least 1 number")
        is_valid = False

    char_count = {}
    for char in password.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    repeating_chars = []
    for char, count in char_count.items():
        if count > 1:
            repeating_chars.append(char)

    if repeating_chars:
        errors.append("These characters appear more than once:")
        for char in repeating_chars:
            errors.append(f"{char}: {char_count[char]} times")
        is_valid = False

    if not is_valid:
        for error in errors:
            print(error)

    return is_valid


main()
