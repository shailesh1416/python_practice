# what is API
# what is module
# How to import module

# importing request module
import requests

# storing email in a variable
email_address = "bhagolaa007@gmai"

# using api to check email is valid or invalid
response = requests.get("https://isitarealemail.com/api/email/validate",params={'email':email_address})

# printing result
print(response.json()['status'])