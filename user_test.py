import unittest # Importing the unittest module

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
        self.new_user= User("Queen-Uwitonze","uwitonzeq@gmail.com","wito123") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"Queen-Uwitonze")
        self.assertEqual(self.new_user.user_email,"uwitonzeq@gmail.com")
        self.assertEqual(self.new_user_password,"wito123")

if __name__ == '__main__':
    unittest.main()
