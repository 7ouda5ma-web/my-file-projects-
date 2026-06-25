import time
def validate_email(email): 
  if "@" and "." in email:    
    return True   
  else:
    return False  
def add_user(name,email):  
  if validate_email(email):    
    print(f"user ''{user_name}' with email '{email}' successfully added")
  else:
    print(f"Invaild email faild ''{email}'' faild.")  

user_name=(input("Enter a user name :"))
user_email=(input("Enter your email :"))
time.sleep(2)
print("Checking your user name....please wait")
time.sleep(2)
print("Validating email adress....please wait")
time.sleep(2)
add_user(user_name,user_email)