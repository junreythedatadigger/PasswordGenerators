# print("This code with generate password for paragraph.")

# text = "Share in suffering as a good soldier of Christ Jesus. No soldier gets entangled in civilian pursuits, since his aim is to please the one who enlisted him."
text = input("Enter paragraph: ")
password = ""
for word in text.split():
    # print(word)
    password += word[0]

print(password)