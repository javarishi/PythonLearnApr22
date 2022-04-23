class InvalidAgeError(Exception):

    def __init__(self, *args, **kwargs):
        super(InvalidAgeError, self).__init__(*args, **kwargs)



class BusinessTypeError(Exception):
    """ Inappropriate argument type. """
    def __init__(self, *args, **kwargs): # real signature unknown
        super(BusinessTypeError, self).__init__(*args, **kwargs)
