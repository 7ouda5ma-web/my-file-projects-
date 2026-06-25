import random
print("welcome to the coin gues in game")
print("choose amethod to toss")
print("1-using random.random()")
print("1-using random.randint()")
choice=input("enter your choice 1 or 2:")
if choice=="1":
  random_number=random.random()
  if random_number>=0.5:
   computer_result="HEADS"
  else:
   computer_result="TAILS"
elif choice=="2":
  if random.randint(0,1)==0:
   computer_result="HEADS"
  else:
   computer_result="TAILS"

else:
  print("invaild choice please select ei ther 1 or 2")

user_choice=input("enter your guess (tails or heads) ") 
if user_choice.lower()==computer_result.lower():
  print("congratulation")
else:
  print("sorry your lost")

print(f"the computer,s coin toss result was:{computer_result}")