class Baseclass1:

    def __init__(self, param):
        self.base1Param = param
        print("Base Class 1 :", param)


    def method_one(self):
        print("Method from Baseclass 1", self.base1Param)