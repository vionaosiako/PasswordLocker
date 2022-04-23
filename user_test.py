import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestContact(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Viona","Osiako","Lioness","Lioness") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Viona")
        self.assertEqual(self.new_user.last_name,"Osiako")
        self.assertEqual(self.new_user.username,"Lioness")
        self.assertEqual(self.new_user.password,"Lioness")
    
    #second test   
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


if __name__ == '__main__':
    unittest.main()