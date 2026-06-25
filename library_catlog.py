library_catlog={}
def add_book():
  while True:
    print("\033[H\033[J",end="")
    isbn=input("Enter ISBN: ")
    tital=input("Enter TITAL:")
    author=input("Enter AUTHOR:")
    library_catlog[isbn]={"tital":tital,"author":author,"available":True}
    print(f"book ('{tital}') by ('{author}') add to the catalog with ISBN ('{isbn}')")
    choice=input("Do you want to add author book? (y/n):")
    if choice.lower()!='y':
      break
def check_out_book():
  while True:
    print("\033[H\033[J",end="")
    isbn=input("Enter Isbn:")
    if isbn in library_catlog:
      if library_catlog[isbn]["available"]:
         library_catlog[isbn]["available"]=False
         print(f"Book('{ library_catlog[isbn]['tital']}')hecked out sucssuflly..")
      else:
        print("sorry,is the book currently checked out ")
    else:
      print("is the book not found in catlog")
    choice=input("Do you want to check out anoyther book ?(y/n):")
    if choice.lower()!='y':
      break
def check_in_book():
  while True:
    print("\033[H\033[J",end="")
    isbn=input("Enter Isbn:")
    if isbn in library_catlog:
      if library_catlog[isbn]["available"]:
         library_catlog[isbn]["available"]=True
         print(f"Book('{ library_catlog[isbn]['tital']}')hecked in sucssuflly..")
      else:
        print("the book is alreay avaliable in library.")
    else:
      print("is the book not found in catlog")
    choice=input("Do you want to check in author book ?(y/n):")
    if choice.lower()!='y':
      break
def list_books():
 while True:
   print("\033[H\033[J",end="")
   print("library_catlog")
   for isbn in library_catlog:
     book_info=library_catlog[isbn]
     print(f"ISN :('{isbn}'), Tital:('{book_info['tital']}') ,Auther: ('{book_info['author']}') , Availbale:('{book_info['available']}') ")
     chioce=input("Do you want to beak to the menu? (y/n):")
     if chioce.lower()=='y':
       break
while True:
  print("Menu:")
  print("1_ Add Book")
  print("2_ Check out Book")
  print("3_ Check in Book")
  print("4_ List Books")
  print("5_ Exit ")
  choice=input("Enter your choice (1-5):")
  if choice=='1':
    add_book()
  elif choice=='2':
    check_out_book()
  elif choice=='3':
    check_in_book()
  elif choice=='4':
    list_books()
  elif choice=='5':
    print("Exitang the program")
    break
  else:
    print("Invalid choice please enter a number between 1 and 5 : ")