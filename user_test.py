import unittest # Importing the unittest module
from user import User # Importing the user class

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
      self.new_person= User("Queen-Uwitonze","uwitonzeq@gmail.com","wito123") # create user object

  def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      self.assertEqual(self.new_person.user_name,"Queen-Uwitonze")
      self.assertEqual(self.new_person.email,"uwitonzeq@gmail.com")
      self.assertEqual(self.new_person.password,"wito123")

  def test_save_user(self):
      '''
      test_save_user test case to test if the user object is saved into
        the user list
      '''
      self.new_person.save_user() # saving the new user
      self.assertEqual(len(User.user_list),1)

  def tearDown(self):

    '''
    tearDown method that does clean up after each test case has run.
    '''
    User.user_list = []

  def test_save_multiple_user_contact(self):

    '''
    test_save_multiple_user-contact to check if we can save multiple user
    objects to our user_list
    '''
    self.new_person.save_user()
    test_person = User("New","new@user.com","muraho") # new user
    test_person.save_user()
    self.assertEqual(len(User.user_list),2)

  def test_delete_user(self):
    '''
    test_delete_user to test if we can remove a user from our use list
    '''
    self.new_person.save_user()
    test_person = User("New","new@user.com","muraho") # new user
    test_person.save_user()

    self.new_person.delete_user()# Deleting a user object
    self.assertEqual(len(User.user_list),1)

  def test_find_person_by_user_name(self):
    '''
    test to check if we can find a user contact by username and display information
    '''

    self.new_person.save_user()
    test_person = User("New","new@user.com","muraho") # new user
    test_person.save_user()

    found_person = User.find_by_user_name("New")

    self.assertEqual(found_person.email,test_person.email)
  

if __name__ == '__main__':
    unittest.main()
