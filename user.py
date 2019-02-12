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
