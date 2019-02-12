import pyperclip

class Credential:
    """
    Class that generates new instances of  credential.
    """
    # Init method up here
    def __init__(self,user_name,email,password):
      self.user_name = user_name
      self.email = email
      self.password = password

    credential_list = [] # Empty contact- credentials list
    # Init method up here
    def save_credential(self):
      '''
      save_user method saves user objects into user_list
      '''
      Credential.credential_list.append(self)


    def delete_credential(self):
      '''
      delete_user method deletes a saved user from the user_list
      '''
      Credential.credential_list.remove(self)


    @classmethod
    def find_by_credential_name(cls,user_name):
      '''
      Method that takes username and returns a user that matches that username.
      Args:
          username: username to search for
      Returns :
          User contact  of person that matches the username.
      '''
      for person in cls. credential_list:
          if person.user_name == user_name:
              return person
    @classmethod
    def copy_email(cls,user_name):
        found_person =  Credential.find_by_user_name(user_name)
        pyperclip.copy(found_person.email)
