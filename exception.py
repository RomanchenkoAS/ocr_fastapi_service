class InvalidLanguage(Exception):
    """ Raised when requested language is invalid or not installed. """
    def __init__(self, message):
        self.message = message
