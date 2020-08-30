
user_name = ["sandeep", "manoj", "diraj", "saroj"] # Admins
pass_code = ["1234", "2345", "3456", "4567"] # passcode for Admins # small changes here

count = 0
while count <3:
    username = input("Enter User name: ")
    username = username.lower()
    count = count+1
    if username == user_name[0]:
        count = 0
        while count <3:
            passcode = str(input("Enter passcode:")) # small changes here.
            if passcode.isdigit(): # adddition here
                count = count + 1
                if passcode == pass_code[0]:
                    break
                else:
                    print("Invalid passcode")
            else:
                print("passcode CONSISTS OF 4 DIGITS") # addition here
        if count == 3:
            print("EXITING")
        break

    else:
        pass


if count == 3: # to input username and and to give three attempts
    print('3 UNSUCCESFUL username ATTEMPTS, EXITING')
    exit()
print(" User name and password verification is successful")

while True: # to write further code
    choice = input("Enter choice:")
    break

