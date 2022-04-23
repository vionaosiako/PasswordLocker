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