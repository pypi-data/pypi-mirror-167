from pscript import py2js



class TestA:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("hello", self.name)


class TestB(TestA):
    def hello2(self):
        print("hello2 from TestB", self.name, self.age)


def foo(a, b=2):
   print(a - b)



print(py2js(TestB))

