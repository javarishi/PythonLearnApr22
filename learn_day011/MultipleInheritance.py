from learn_day011.BaseClass1 import Baseclass1
from learn_day011.Baseclass2 import Baseclass2
from learn_day010.CustomerHirarchy import GoogleMapValidation as Google


# In case of conflict - first parent takes precedence
# Tip = use specific Parent First and Generic Parent Later
class ChildClass(Baseclass1, Baseclass2, Google):

    def __init__(self, param, childParam):
        Baseclass1.__init__(self, param)
        Baseclass2.__init__(self, param)
        self.child_param = childParam
        print("Child Class Instantiated :", self.child_param)


    def method_one(self):
        Baseclass1.method_one(self)
        Baseclass2.method_one(self)
        print("Method from ChildClass", self.child_param)


c1 = ChildClass("parentParam", "childParam")
c1.method_one()

