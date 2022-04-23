class User:
    """
    Class that generates new instances of user
    """

    def __init__(self,first_name,last_name,username,password):

        '''
        __init__ method that helps us define properties for our objects.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password