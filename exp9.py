import re

file = open("input.txt", "r")
text = file.read()
file.close()

emails = re.findall(r'\S+@\S+\.\S+', text)

print("Email addresses found:")

for email in emails:
    print(email)

print("Total emails:", len(emails))
