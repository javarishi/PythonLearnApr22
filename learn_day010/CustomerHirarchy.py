class Customer:

    def __init__(self, age, gender, race, purchasePower):
        self.age = age
        self.gender = gender
        self.race = race
        self.purchasePower = purchasePower
        print("New Customer is Created", self.age, self.race, self.purchasePower, self.gender)


    def discount(self):
        print("No Discount for New Customer with age :: ", self.age)
        return "No Discount for New Customer"


class PreferredCustomer(Customer):

    def __init__(self, age, gender, purchasePower, name, email, address):
        Customer.__init__(self, age, gender, "American", purchasePower)
        self.name = name
        self.email = email
        self.address = address
        print("New PreferredCustomer is Created", self.name, self.email, self.address)


    def mail_discount_coupons(self):
        print("Coupons shipped to {} and email sent to {} ".format(self.address, self.email))


    def validation(self):
        print("Basic validation API for ", self.address)


    def discount(self):
        print("Overridden discount rates for Preferred Customer " , self.name)
        return "{} has {} % discount".format(self.name, "3")


class GoogleMapValidation:

    def validate(self, address):
        print("Google Map Validation for {} ".format(address))


class CreditCardCustomer(PreferredCustomer, GoogleMapValidation):

    def __init__(self, age, gender, purchasePower, name, email, address, ssn):
        PreferredCustomer.__init__(self, age, gender, purchasePower, name, email, address)
        self.ssn = ssn
        print("Credit Card Customer Created")


    def discount(self):
        print("Overridden discount rates from Preferred Customer " , self.name)
        return "{} has {} % discount as CC Customer".format(self.name, "5")


    def validation(self):
        PreferredCustomer.validation(self)
        print("Google Maps validation API for ", self.address)


pCust01 = CreditCardCustomer(30, 'M', 'Good', "Niel", "niel@nasa.com", "111 Moon Land Prkwy, FL", "3204309284")
print(pCust01.discount())
pCust01.mail_discount_coupons()
pCust01.validation()