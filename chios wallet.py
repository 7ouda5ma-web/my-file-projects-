import random

print("welcome to the whose wallet ")

print("you will give a list of names and ,and iwill pick a person to pay")

names_string=input("enter names separated by commas:").split(',')

print(f"please ask ''{random.choice(names_string)}' to take his wallet out .dinner is on him ")
