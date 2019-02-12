#!/usr/bin/env python3.6

from user import User

def create_person(user_name,email,password):
  '''
  Function to create a new contact
  '''
  new_person = User(user_name,email,password)
  return new_person

def save_persons(person):
    '''
    Function to save contact
    '''
    person.save_user()

def del_person(person):
    '''
    Function to delete a contact
    '''
    person.delete_user()

def find_person(user_name):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.find_by_user_name(user_name)

def check_existing_persons(number):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.person_exist(user_name)

def display_persons():
    '''
    Function that returns all the saved contacts
    '''
    return User.display_persons()

def copy_email(user_name):
  '''
  function that handles the behavior of copy the email 
  '''
  return User.display_person(user_name)

def main():
    print("Hello Welcome to your password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("....User name ....")
                            user_name = input()

                            print("....Email address....")
                            e_address = input()

                            print("....password....")
                            password = input()


                            save_persons(create_person(user_name,e_address,password)) # create and save new contact.
                            print ('\n')
                            print(f"New User Account {user_name} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_persons():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for person in display_persons():
                                            print(f"{person.user_name} .....")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_user_name= input()
                            if check_existing_persons(search_user_name):
                                    search_person = find_person(search_user_name)
                                    print(f"{search_person.user_name}")
                                    print('-' * 20)

                                    print(f"Email address.......{search_person.email}")
                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
    
if __name__ == '__main__':
      main()