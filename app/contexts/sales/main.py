from infrastructure.di.container import Container

def init_sales_context():
    container = Container()

class SalesContext:

    def __init__(self):
        self.container = Container()
        print("Sales Context Initialized")
