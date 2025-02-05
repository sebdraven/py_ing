from my_packake.my_class import MyClass
from interface import Interface

class MySubClass(Interface):
    def __init__(self):
        print('MySubClass.__init__')
        super().__init__()

    def first_method(self):
        print('MySubClass.first_method')

class Operation:
    def __init__(self,a:int,b:int):
        self._a = a
        self._b = b
    
    @staticmethod
    def add(a,b) -> int:
        return a+b
    @staticmethod
    def iter_list(numbers:list):
        for i in numbers:
            yield i
    @staticmethod
    def read(file_path:str):
        with open(file_path,'r') as fh:
            for line in fh.readlines():
                print(line)

if __name__ == "__main__":
    Operation.read('test.txt')  
    my_class = MyClass()
