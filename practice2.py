import phonenumbers
from phonenumbers import geocoder
a = input("enter phone number")
phone_number = phonenumbers.parse(a)
print(geocoder.description_for_number(phone_number, "en"))


