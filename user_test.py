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
        
    #third test
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","0712345678","test@user.com") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
    # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []

    # other test cases here
    def test_save_multiple_user(self):
            '''
            test_save_multiple_user to check if we can save multiple user
            objects to our user_list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","vee","vee") # new user
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
            
    #Fourth test
    # More tests above
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from user list
            '''
            self.new_user.save_user()
            test_user = User("Test","user","vee","vee") # new contact
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)
            
    #fifth test
    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Test","user","vee","vee") # new user
        test_user.save_user()

        found_user = User.find_by_username("vee")

        self.assertEqual(found_user.password,test_user.password)     
    



if __name__ == '__main__':
    unittest.main()