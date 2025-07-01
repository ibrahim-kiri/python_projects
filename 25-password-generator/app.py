import random
import string

def generate_password(length, use_lowercase,use_uppercase,use_numbers,use_special):
    chars = ""
    
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_numbers:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        print("⚠️ Ooops! No character types selected. Using lowercase letters by default!")
        chars = string.ascii_lowercase

    password = ""
    for _ in range(length):
        password += random.choice(chars)

    return password

def check_password_strength(password):
    score = min(len(password) / 16, 1.0)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    variety = (has_lower + has_upper + has_digit + has_special) / 4.0

    final_score = (score * 0.6) + (variety * 0.4)

    if final_score >= 0.8:
        return "💪 Your password is STRONG! 💪"
    elif final_score >= 0.6:
        return "👍 Your password is GOOD! 👍"
    elif final_score >= 0.4:
        return "👌 Your password is AVERAGE. 👌"
    else:
        return "⚠️ Your password is WEAK! ⚠️ Needs Improvement."

def get_yes_no_input(question):
    while True:
        response = input(question + "(y/n): ").lower()
        if response in ["yes", "y"]:
            return True
        elif response in ["no", "n"]:
            return False
        else:
            print("I didn't get that! Please enter 'y' or 'n'.")

def main():
    print("\n ==== 🔐 PASSWORD GENERATOR 🔐 ====")
    print("✨ Create super strong and secure passwords with ease! ✨\n")

    while True:
        try:
            length = int(input("\nEnter passowrd length (8-30): "))
            if 8 <= length <= 30:
                break
            else:
                print("⚠️ Please choose a length between 8 and 30!")
        except ValueError:
            print("❌ Oops! Please enter a number, like 12 or 16.")

    print("\n Let's customize your password!")

    use_lowercase = get_yes_no_input("Include lowercase letters (a-z)? ")
    use_uppercase = get_yes_no_input("Include uppercase letters (A-Z)? ")
    use_numbers = get_yes_no_input("Include numbers(0-9)? ")
    use_special = get_yes_no_input("Include special character (!@$#%)? ")

    print("\n 🧙‍♂️ Generating your magical password...🧙‍♂️")
    password = generate_password(length,use_lowercase,use_uppercase,use_numbers,use_special)

    print("\n=== YOUR NEW PASSWORD 🎉")
    print(f"🔑 {password}")

    strength = check_password_strength(password)
    print(f"💪 Strength: {strength}")

    # Step 5: Show password tips
    print("\n 📝=== PASSWORD TIPS ===📝")
    print("🚫 Never use the same password for multiple accounts")
    print("🛅 Consider using a password manager")
    print("🔄 Change your passwords regularly")
    print("🤫 Even strong password need to be kept secret!")

    if get_yes_no_input("\nWould you like to create another awesome password? "):
        main()
    else:
        print("\n🎉 Thank you for using the Super Fun Password Generator! Stay secure!")

main()