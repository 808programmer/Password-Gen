import random as rand
import datetime as dt
import time as tm

date_time = dt.datetime.now()
def password_generator():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s",
               "t","u","v","w","x","y","z"]
    numbers = [0,1,2,3,4,5,6,7,8,9]
    symbols = ["!","@","#","$","%","^","&","*","/",".","(",")","?"]
    print("Welcome to Password Generator.\n~ Written by Khalil Francis")
    print(date_time.strftime("%A, %B %d, %Y %I:%M%p\n"))
    tm.sleep(1)

    num_letters = int(input("How many letters would you like your password to be?\n"))
    num_symbols = int(input("How many symbols would you like your password to be?\n"))
    num_numbers = int(input("How many numbers would you like your password to be?\n"))

    password = ""
    new_password = ""
    for char in range(0,num_letters):
        password += rand.choice(letters)

    for char in range(0,num_symbols):
        password += rand.choice(symbols)

    for char in range(0,num_numbers):
        password += str(rand.choice(numbers))

    pass_list = list(password)
    rand.shuffle(pass_list)

    for i in pass_list:
        new_password += i

    print(f"Your password is: {new_password}")

if __name__ == "__main__":
    password_generator()