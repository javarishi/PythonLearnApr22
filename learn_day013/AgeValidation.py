from learn_day013.InvalidAgeError import InvalidAgeError

def validate_age(age):
    int_age = int(age)
    if int_age > 18:
        return "Valid Age"
    else:
        raise InvalidAgeError("Invalid Age Provided")


validate_age(17)