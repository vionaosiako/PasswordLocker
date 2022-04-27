from user import User, Credentials

def create_new_user(username,password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()
def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
def login_user(username,password):
    """
    function that checks whether a user exist and then login the user in.
    """

    check_user = Credentials.verify_user(username,password)
    return check_user

def create_new_credential(account,userName,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account,userName,password)
    return new_credential
def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()
def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)
def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)


def passlocker():
    print("Welcome to Password Locker.\n Please select one to proceed.\n CA - Create New Account  \n LI - Log IN  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('-' * 50)
        username = input("Username: ")
        while True:
            print(" TP - Type your pasword: ")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            
            else:
                print("Invalid password.")
        save_user(create_new_user(username,password))
        print("_"*50)
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*50)
    elif short_code == "li":
        print("_"*50)
        print("Enter your Username and Password to log in:")
        print('_' * 50)
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username}.Welcome To Password Locker")  
            print('\n')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("_"*50)
            print("Account name ....")
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - Tyour pasword if you already have an account: ")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Password\n")
                    break
                
                else:
                    print("Invalid password")
            save_credentials(create_new_credential(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_accounts_details():
                print("List of accounts: ")

                print('_' * 50)
                print('_'* 50)
                for account in display_accounts_details():
                    print(f" Account:{account.account} \n Username:{username}\n Password:{password}")
                    print('_'* 50)
                print('_' * 50)
            else:
                print("No credentials saved")
        elif short_code == "fc":
            print("Enter the Account Name you would to search")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name you want to delete")
            search_name = input().lower()
            if find_credential(search_name):
                search_credential = find_credential(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("Credential does not exist")

        
        elif short_code == 'ex':
            print("Thanks You for using Password Locker")
            break
        else:
            print("Wrong Details")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    passlocker()