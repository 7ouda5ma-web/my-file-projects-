colors=[]
fav_color=input("add the first color you like :")
colors.append(fav_color)
cohice=input("add you want to add more color/?yes or no:").lower()
if cohice=="yes":
    fav_color=input("add amother color to the list:")
    colors.append(fav_color)
    print("the colors you like are ")
    print(colors)
else :
    print("the colors you like is ")
    print(colors)