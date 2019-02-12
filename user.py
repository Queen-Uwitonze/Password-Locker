class User:
    """
    Class that generates new instances of users.
    """

    users_list = [] # Empty contact list
    # Init method up here
    def __init__(self,user_name,email,password):
      self.user_name = user_name
      self.user_email = email
      self.user_password = password
     
