class User:
    """
    Class that generates new instances of users.
    """
    # Init method up here
    def __init__(self,user_name,email,password):
      self.user_name = user_name
      self.user_email = email
      self.user_password = password

    user_list = [] # Empty contact-users list
    # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)
     
