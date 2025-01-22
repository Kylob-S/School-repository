import random
import string
#imports for Password

name = input("Enter your name: ")
print("Hello " + name + "!")

if name:
    print("Would you like me to generate a random password for you?\n (yes/No)")
    response = input("Enter your response:\n ")

    if response == "yes":


        password_length = int(input("Enter your password length:\n "))#User tells the Generator how many characters to generate.
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=password_length)) #Specifies how many characters to grab.
                                             #Combines letters and numbers.
        print("Generating Random Password...")

        print(f"Your password is: {password}")#Displays the Generated password.
    else:
        print("Okay then")#Response to anything but "yes"
