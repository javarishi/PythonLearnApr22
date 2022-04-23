class Simple:

    def __init__(self):
        print("Simple Class")

    def simple_method(self):
        print("Simple Method")


class AnotherSimple:
    def __init__(self):
        print("AnotherSimple Class")

    def simple_method(self):
        print("AnotherSimple Method")

    def anothersimple_method(self):
        print("AnotherSimple Method")

class SuperSimple(Simple, AnotherSimple):

    def __init__(self):
        super(SuperSimple,self).__init__()
        AnotherSimple.__init__(self)
        print("Super Simple Constructor")


    def simple_method(self):
        super(SuperSimple, self).simple_method()


    def anothersimple_method(self):
        super(SuperSimple, self).anothersimple_method()
        print("AnotherSimple Method from child")

ss = SuperSimple()
ss.anothersimple_method()