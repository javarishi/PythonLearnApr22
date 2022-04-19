class RetailStore:
    # Propertise / variables / fields

    def __init__(self):
        self.store_name = "Rite Aid"
        print('this is initializer function also called as Constructor')

    # functions
    def discount(self):
        print("Discount for new customer is 2% in {} ".format(self.store_name))


riteAid = RetailStore()
print(riteAid.store_name)
riteAid.discount()

walmart = RetailStore()
walmart.store_name = "Wlamart Inc."
print(walmart.store_name)
walmart.discount()

print("Checking original value: " , riteAid.store_name)
