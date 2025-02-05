class MyClass:
    def __init__(self):
        print('MyClass.__init__')

class MySubClass(MyClass):
    def __init__(self):
        print('MySubClass.__init__')
        super().__init__()

class SecondSubClass():
    def __init__(self):
        print('SecondSubClass.__init__')
        