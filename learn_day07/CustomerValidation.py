def validate(name, zipcode, county, city):
    if str(name).isalpha():
        print("Name {} is Valid".format(name))
    else:
        print("Name {} is inValid".format(name))

    if str(zipcode).isnumeric() and len(str(zipcode)) == 5:
        print("Zipcode {} is Valid".format(zipcode))
    else:
        print("Zipcode {} is inValid".format(zipcode))

    print("county {} is Valid".format(county))
    print("city {} is Valid".format(city))


def customer_validation(*args):
    print(args, type(args))
    for eachVar in args:
        print("{} is valid".format(eachVar))


customer_validation("Niel", 33900, "Smyrna", "Atlanta", "Georgia")


def customer_validation_keys(**kwargs):
    print(kwargs, type(kwargs))
    for eachVar in kwargs:
        print("{} is valid".format(eachVar))


# customer_validation("Niel", 33900, "Smyrna", "Atlanta", "Georgia")
customer_validation_keys(name="Niel", zipcode=30089, city="Atlanta")

# 1. Can you use both args and kwargs in same method
# 2. If yes, what should be the sequence - normal, *args, **kwargs

def customer_validation_final(name, zipcode, *args, country="USA", **kwargs, ):
    print(name)
    print(zipcode)
    print(args)
    print(kwargs)
    print(country)

customer_validation_final("RISHI", 33639, "Hillsborrow", "Oldsmar", state="FL")