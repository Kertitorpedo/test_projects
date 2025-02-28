import time

# Enter your new details
mixed_list = []
username = input("Please register your username:")
username = username

password = input("Please type a new password:")
password = password

username_input = ""
while username_input != username:
    username_input = input("Enter your username:")
    if username_input != username:
        print("Checking...")        # Giving some time to the machine to check it in the database (verify)
        time.sleep(1)
        print("Couldn't find your username.. Please try again")     #If you type a different username it won't match so it will give another option
    elif username_input == username:
        print("Checking...")
        time.sleep(1)
        print("Username accepted")      #If the username is the same what was given in input, then it accepts and goes to the following step

#same method, with the password
user_input = ""
while user_input != password:
    user_input = input('Enter your password: ')
    if user_input != password:
        print("Wrong password. Try again!")
    elif user_input == password:
        print("Please wait...")
        time.sleep(1)
        print("You've successfully logged in.")
        print("Just a second...")
# if both of them are valid, it will sign you in.
if user_input == password and username_input == username:
    time.sleep(2)
    print("Access granted!!!")

mixed_list = f"Username: {username} \nPassword: {password}"

# Making a file where it will store the data (in this case a text file)
with open("data_log_in.txt", "w") as file:
    for item in mixed_list:
        file.write(str(item))

# Reading data from the text file
with open("data_log_in.txt", "r") as file:
    stored_data = file.readlines()

print("Data stored!", stored_data)