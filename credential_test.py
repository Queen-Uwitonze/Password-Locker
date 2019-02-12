import unittest # Importing the unittest module
from  credential import  Credential # Importing the user class
import pyperclip

class Test Credential(unittest.TestCase):

  '''
  Test class that defines test cases for the user class behaviours.

  Args:
      unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
      '''
      Set up method to run before each test cases.
      '''
      self.new_person=  Credential("Queen-Uwitonze","uwitonzeq@gmail.com","wito123") # create user object

  def test_init(self):
      '''
      test_init test case to test if the object is initialized properly
      '''

      self.assertEqual(self.new_person.user_name,"Queen-Uwitonze")
      self.assertEqual(self.new_person.email,"uwitonzeq@gmail.com")
      self.assertEqual(self.new_person.password,"wito123")

  def test_save_ credential(self):
      '''
      test_save_user test case to test if the user object is saved into
        the user list
      '''
      self.new_person.save_ credential() # saving the new user
      self.assertEqual(len( Credential. credential_list),1)

  def tearDown(self):

    '''
    tearDown method that does clean up after each test case has run.
    '''
     Credential. credential_list = []

  def test_save_multiple_ credential_contact(self):

    '''
    test_save_multiple_user-contact to check if we can save multiple user
    objects to our user_list
    '''
    self.new_person.save_ credential()
    test_person =  Credential("New","new@user.com","muraho") # new user
    test_person.save_ credential()
    self.assertEqual(len( Credential. credential_list),2)

  def test_delete_ credential(self):
    '''
    test_delete_user to test if we can remove a user from our use list
    '''
    self.new_person.save_ credential()
    test_person =  Credential("New","new@user.com","muraho") # new user
    test_person.save_ credential()

    self.new_person.delete_ credential()# Deleting a user object
    self.assertEqual(len( Credential. credential_list),1)

  def test_find_person_by_user_name(self):
    '''
    test to check if we can find a user contact by username and display information
    '''

    self.new_person.save_ credential()
    test_person =  Credential("New","new@user.com","muraho") # new user
    test_person.save_ credential()

    found_person = User.find_by_user_name("New")

    self.assertEqual(found_person.email,test_person.email)

  def test_copy_email(self):
        '''
        Test to confirm that we are copying the email address from a found user contact
        '''
        self.new_person.save_ credential()
        Credential.copy_email("Queen-Uwitonze")
        self.assertEqual(self.new_person.email,pyperclip.paste())
  


          


if __name__ == '__main__':
    unittest.main()
