import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_person= User("Queen-Uwitonze","uwitonzeq@gmail.com","wito123") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_person.user_name,"Queen-Uwitonze")
        self.assertEqual(self.new_person.user_email,"uwitonzeq@gmail.com")
        self.assertEqual(self.new_person.user_password,"wito123")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_person.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()
