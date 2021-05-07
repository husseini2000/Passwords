import re
import csv


def get_data():
    file = list(csv.reader(open("Password.csv")))
    tmp = []
    for x in file:
        tmp.append(x)
    return tmp


def add_record(us_num, password):
    new_record = us_num + "," + password + "\n"
    file = open("Password.csv", "a")
    file.write(new_record)
    file.close()


def create_password():
    password = input("Enter a new password: ")
    flag = 0
    more = True
    while more:
        if len(password) >= 8:
            flag += 1
        if re.search("[a-z]", password):
            flag += 1
        if re.search("[A-Z]", password):
            flag += 1
        if re.search("[0-9]", password):
            flag += 1
        if re.search("[_@$]", password):
            flag += 1
        if not re.search("\s", password):
            flag += 1

        if flag in range(0, 3):
            print("A rejected password")
            # main()
        elif flag in range(3, 5):
            print("This password could be improved.")
            answer = input("Do you want try again (y/n): ")
            if answer == 'n':
                more = False
        else:
            print("A strong password")
            return password


def create_id(tmp):
    """ Get ID from the user , and
        check if it's existed in the list """
    user_id = 0
    again = True
    while again:
        user_id = input("Enter a new user ID: ")
        inlist = False
        row = 0
        for y in tmp:
            if user_id in tmp[row][0]:
                inlist = True
                print("Sorry! ID is already exist in list.")
            row += 1
        if not inlist:
            again = False
    return user_id


def find_id(tmp):
    user_id = ""
    again = True
    while again:
        search_id = input("Enter a user ID you looking about: ")
        inlist = False
        row = 0
        for y in tmp:
            if search_id in tmp[row][0]:
                inlist = True
            row += 1
        if inlist:
            user_id = search_id
            again = False
        else:
            print(search_id, " Is not in the list.")
    return user_id


def change_pass(user_id, tmp):
    if user_id != "":
        password = create_password()
        userId = user_id.index(user_id)
        tmp[userId][1] = password
        file = open("Password.csv", "w")
        x = 0
        for row in tmp:
            new_row = tmp[x][0] + ", " + tmp[x][1] + "\n"
            file.write(new_row)
            x += 1
        file.close()


def display_IDs():
    tmp = get_data()
    x = 0
    for x in tmp:
        print(tmp[x][0])
        x += 1


def get_operation_choice():
    """
        Show menu of operations user can select from them.
        Performs some verifications of the input."""
    input_ok = False
    user_selection = 0
    while not input_ok:
        print('Menu Options are:')
        print('\t1. Create a new User ID')
        print('\t2. Change a password')
        print('\t3. Display all User IDs')
        print('\t4. Quit')
        print('-----------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4'):
            input_ok = True
        else:
            print('Invalid Input (must be 1 - 4)')
    print('-----------------')
    return user_selection


def main():
    """ Call specific operation for user,
        if the operation not exists print error message"""
    # file = open("Password.csv", "w")
    # file.close()
    tmp = get_data()
    flag = False
    while not flag:
        menu_choice = get_operation_choice()
        if menu_choice == '1':
            us_id = create_id(tmp)
            us_pass = create_password()
            add_record(us_id, us_pass)
        elif menu_choice == '2':
            us_id = find_id(tmp)
            change_pass(us_id, tmp)
        elif menu_choice == '3':
            display_IDs()
        elif menu_choice == '4':
            flag = True
        else:
            print("Incorrect option!")
    print('=================')


main()
