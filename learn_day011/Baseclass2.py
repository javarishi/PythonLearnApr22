class Baseclass2:

    def __init__(self, param):
        self.base2Param = param
        print("Base Class 2 :", param)


    def method_one(self):
        print("Method from Baseclass 2", self.base2Param)