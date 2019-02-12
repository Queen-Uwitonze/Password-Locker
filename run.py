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


# if __name__ == '__main__':
#     main()