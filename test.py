# Personalized Error Handling File Reader

user_name = "Madge Mutemi"
business_name = "Class Measures Limited"

filename = input("Hi Madge 👋, please enter the name of the file you want to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print(f"\n📂 Successfully read the file: {filename}")
        print(f"\n👩‍💼 Hello {user_name} from {business_name}!")
        print("Here's what's inside your file:\n")
        print(content)
except FileNotFoundError:
    print(f"\n🚫 Oops! The file '{filename}' does not exist. Please check the name and try again.")
except PermissionError:
    print(f"\n🔒 Permission denied when trying to read '{filename}'.")
except Exception as e:
    print(f"\n⚠️ An unexpected error occurred: {e}")
