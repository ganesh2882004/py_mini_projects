contacts = {}


def  Add_Contact ():
        name = input("Enter the name : ")
        number =input("Enter the phone number :")
        if name in contacts:
              print("name already exist")
        else:
              contacts[name] = number
              print("contact added")
def  View_Contacts ():  
      for i,name in enumerate(sorted(contacts),start=1)  :
            print(f"Contact {i}")
            print(f"Name: {name}")
            print(f"Number: {contacts[name]}")

def  Search_Contact (): 
    name = input("Enter the contact name  you want to scarch : ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Number: {contacts[name]}")
    else:
        print("name does not exist")
def  Update_Contact ():
        name = input("Enter the name you want to update : ")
        number =input("Enter the phone number :")
        if name in contacts:
              contacts[name] = number
              print("contact updated")
        else:
          print("name does not exist")

def  Delete_Contact ():
    name = input("Enter the name you want to delete : ")
    if name in contacts:
          contacts.pop(name)
          print("contact deleted")
    else:
          print("name does not exist")



            

def Contact_Book ():
    
    print("WELCOME TO Contact Book")
    while True:

        print("what do u want to from us from the menue")
        print("""
        1. Add Contact
        2. View Contacts
        3. Search Contact
        4. Update Contact
        5. Delete Contact
        6. Exit
        """)
        choice = int(input("Please select  the number of the menue that u want from os : "))
        
        if choice == 1:
            Add_Contact ()
        elif choice == 2:
           View_Contacts ()
        elif choice == 3:
            Search_Contact ()
        elif choice == 4:
            Update_Contact ()
        elif choice == 5:
            Delete_Contact ()
        elif choice == 6 :    
            print("Thank you for using Contact Book.")
            break
        else :
            print("Invalid choice. Please try again.")



Contact_Book ()  