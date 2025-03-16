from shared.errors.base_error import BaseError

class UnexpectedError(BaseError):
    """Unexpected Error class for all exceptions in the application."""
    
    def __init__(self, exception: Exception):
        self.message = exception.args[0]
        self.stacktrace = exception.args[1]