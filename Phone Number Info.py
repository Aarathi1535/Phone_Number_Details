import phonenumbers
from phonenumbers import carrier, geocoder, timezone
mobileNo = input("Enter the phonenumber with country code(+xx xxxxxxxxxx) to fetch details :")
mobileNo = phonenumbers.parse(mobileNo)
if phonenumbers.is_valid_number(mobileNo):
    print("The Phonenumber belongs to region:", timezone.time_zones_for_number(mobileNo))
    print("Service Provider:", carrier.name_for_number(mobileNo, "en"))
    print("The Phonenumber belongs to country:", geocoder.description_for_number(mobileNo,"en"))
else:
    print("You Phonenumber is invalid. Please enter a valid phonenumber.")




