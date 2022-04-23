class User:
    """
    Class that generates new instances of user
    """
    
    user_list = [] # Empty user list

    def __init__(self,first_name,last_name,username,password):

        '''
        __init__ method that helps us define properties for our objects.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        
    user_list = [] # Empty user list
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
    def find_by_username(cls,username):
        '''
        Method that takes in username and returns a user that matches that username.

        '''

        for user in cls.user_list:
            if user.username == username:
                return user
            
    #check if a user object actually exists   
    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("Test","user","vee","vee") # new user
        test_user.save_user()

        user_exists = User.user_exist("vee")

        self.assertTrue(user_exists)
