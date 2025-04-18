# Example personalized greeting and business info
user_name = "Madge Mutemi"
business_name = "Class Measures Limited"
contact = "+254729088784"
email = "madge.mutemi@gmail.com"

# Open the original file in read mode
with open('original.txt', 'r') as file:
    content = file.read()

# Modify the content by adding personalized information
modified_content = f"Hello {user_name},\n\n"
modified_content += f"Welcome to {business_name}!\n"
modified_content += f"Feel free to reach out through:\n"
modified_content += f"Contact: {contact}\nEmail: {email}\n\n"
modified_content += "We hope this file helps you with your next steps:\n\n"
modified_content += content

# Open a new file in write mode and write the modified content
with open('modified.txt', 'w') as new_file:
    new_file.write(modified_content)

print("Your personalized file has been successfully created!")
