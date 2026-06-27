print("welcome to place the rabbit")
row=['🍀','🍀','🍀'],['🍀','🍀','🍀'],['🍀','🍀','🍀']
print(row[0],'\n', row[1],'\n', row[2])
print("where should the rabbit go?🐇")
now=input("please enter the row and column ")
print("success......")
tot=int(now[0])
tom=int(now[1])
row[tot-1][tom-1]='🐇'
print(row[0],'\n', row[1],'\n', row[2])
