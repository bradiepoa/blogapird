import random
from django.core.mail import EmailMessage

def generateOtp():
    otp =""
    for i in range(6):
        otp +=str(random.randint(1, 9))
    return otp


