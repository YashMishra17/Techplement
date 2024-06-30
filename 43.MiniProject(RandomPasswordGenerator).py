import random
import string

pass_len= 17
charValues = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)

print("your random password is:", password)    
