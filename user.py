import pyperclip

class User:
    """
    Class that generates new instances of users.
    """
    # Init method up here
    def __init__(self,user_name,email,password):
      self.user_name = user_name
      self.email = email
      self.password = password

    user_list = [] # Empty contact-users list
    # Init method up here
    def save_user(self):

      '''
      save_user method saves user objects into user_list
      '''
      User.user_list.append(self)


    def delete_user(self):

      '''
      delete_user method deletes a saved user from the user_list
      '''

      User.user_list.remove(self)


    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes username and returns a user that matches that username.

        Args:
            username: username to search for
        Returns :
            User contact  of person that matches the username.
        '''
        for person in cls.user_list:
            if person.user_name == user_name:
                return person
    @classmethod
    def copy_email(cls,user_name):
        found_person = User.find_by_user_name(user_name)
        pyperclip.copy(found_person.email)
    
    @classmethod
    def display_persons(cls):
        '''
        method that returns the contact list
        '''
        return cls.user_list

    @classmethod
    def person_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            number: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for person in cls.user_list:
            if person.user_name == user_name :
                    return True

        return False