# Simple project that print hello-world

__version__ = "0.2.0"


class HelloWorld:

    def __init__(self, message):
        self.message = message

    def log(self):
        print(self.message)
        return self.message
