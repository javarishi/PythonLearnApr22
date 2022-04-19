class Store:

    def __init__(self, sName, sNumber):
        self.store_name = sName
        self.store_number= sNumber
        self.discount_percent = 5
        print("Store is Initialized with {} and {} ".format(self.store_name, self.store_number))

    # function which takes self parameter are called as instance / object function
    def discounts(self, isStoreNew):
        if isStoreNew:
            print("New Store hence discount is provided {} %".format(self.discount_percent))
            return self.discount_percent
        else:
            print("Old Store hence NO discount is provided")
            return 0

    @classmethod
    def company_name(cls):
        print("Company Name :: The Home Depot INC.")
        return "Home Depot Inc."


s1 = Store("Cumberland Store", 121)
s1.discounts(True)
Store.company_name()
print(type(s1))
print(type(s1.discounts))
s2 = s1
s2.discounts(False)