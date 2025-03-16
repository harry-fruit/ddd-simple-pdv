class BaseError(Exception):
    """Base Error class for all exceptions in the application."""
    
    def __init__(self, message: str, stacktrace: str):
        self.message = message
        self.stacktrace = stacktrace
