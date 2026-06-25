print("""
      
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████""")
print("welomeb to you the isLAND\n")

door=input("were are you two the door 🚪 red or🚪 blue door::").lower()

print(f"you are is choice door the {door}. ")

if door=="red":
  
  print("greet!correct open the door")

  box=input("here ara three boxes in font you .choose one of thme 🎁 white or 🎁  balck or 🎁green:\n").lower()

  if box=="white":

    print("great!you opend box filled with(money)💰💰💰💰💰💰💰.")

  elif box=="green":

    print("oops!you opend box filled with(snckes)🐍🐍🐍🐍🐍🐍🐍. ")

  elif box=="balck":

    print("oops!you opend box filled with (spider)🕷🕷🕷🕸🕸🕸🕸." )

  else:

    print("invatid choice!🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️.")

  money=int(input("how many to the money big.\n"))

  if money==7:

    print("greet!conrats the money.")

  else :

    print("strong!the treasures is locked🏴‍☠️🗻🗻.")

  pin=int(input("enter is the pasword to the cave.\n"))

  if pin==2009:

    print("greet!open the cave(qukly output🏃‍♀️🏃‍♀️🏃‍♀️🏃‍♀️.)")

  else:
     
     print("oops!tryaganthelfel.")

else :
  
  print("invatid choice!🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️🤷‍♀️.")

  print("oops!game over.")
