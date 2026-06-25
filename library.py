library=[]
b_k=input("enter the name of a bok you own:")
library.append(b_k)
b_k=input("enter the name of another book you own(or press 'enter' toskip):")
if b_k:
  library.append(b_k)
print("your library", library )
wishlist=[]
b_future=input("enter the name of abook you wish to have in the future: ")
wishlist.append(b_future)
b_future=input("enter the name of abook you wish to have in the future(or press'enter'to skip )")
if b_future:  
   wishlist.append(b_future)
print(f"your wishlist{wishlist}")
give_book=input("enter the name of a book from your library you wish to (r press'ener' to skip):")
if give_book in wishlist:    
   library.append(give_book)
   wishlist.remove(give_book)
print(f"updated librery {library}")
print(f"updated list_future{wishlist}")
donate_book=input("enter the name book from your library you wish to donate(or press'entre')")
if donate_book in library:
   library.remove(donate_book)
print(f"final library after donations {library}")