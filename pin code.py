import random
user_pin=int(input("enter 4 digiht pin code\n"))
pin=random.randint(1000,9999)
if len(str(user_pin))!=4:
    print("pleas enter 4 digint")
elif pin==user_pin:
    print("correct pin code")
else :
    print("in correct pin code")
    print(pin)