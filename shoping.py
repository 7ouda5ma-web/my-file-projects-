bsket=[['apples','bananas'],['milk','water']]
print(bsket)
enter=input("press enter to continue.....")
print("here is the updated basket")
bsket[0].insert(0,'oranges')
bsket[0].insert(3,"kiwis")
bsket[1].insert(0,"coffee")
bsket[1].remove("water")
bsket[1].append('tea')
bsket.append([1,2,3])


print(bsket)