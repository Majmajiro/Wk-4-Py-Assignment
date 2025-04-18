# Personalized Error Handling with Logging
user_name = "Madge Mutemi"
log_file = "error_log.txt"

filename = input("Hello Madge 👋, please enter the filename you want to read: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        print("\nFile content:\n" + "-"*30)
        print(content)
except FileNotFoundError:
    error_message = f"[FileNotFoundError] '{filename}' not found.\n"
    print(f"\nOops! The file '{filename}' does not exist.")
    with open(log_file, 'a') as log:
        log.write(error_message)
except PermissionError:
    error_message = f"[PermissionError] Cannot read '{filename}'.\n"
    print(f"\nSorry, you don’t have permission to read '{filename}'.")
    with open(log_file, 'a') as log:
        log.write(error_message)
except Exception as e:
    error_message = f"[{type(e).__name__}] {str(e)}\n"
    print(f"\nAn unexpected error occurred: {e}")
    with open(log_file, 'a') as log:
        log.write(error_message)
else:
    print("\nFile read successfully! 🎉")
