#*** Phone Book Menu ***
#Enter 1,2,3 or 4:
#nter 1 To Display Your Contacts Records
#Enter 2 To Add a New Contact Record a new contact
#Enter 3 To search your contacts
#Enter 4 To delete
#enter 5 t0 modify
#enter 6 to quit
from os import remove, write


file_name = "c:/users/adamp/Documents/pythom/phonebook.txt"
file1 = open(file_name, "a+")
file1.close
def show_main_menu():
    ''' Show main menu for Phone Book Program '''
    print("\n   WELCOME TO MY PHONEBOOK \n"+
          "author: Group 2 Beng 20 COE 1 \n"+
          "------------------------------------------\n"+
          "Enter 1,2,3,4,5 or 6:\n"+
          "Enter 1 To Display Your Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To search your contacts\n"+
          "Enter 4 To delete your contacts\n"+
          "Enter 5 To modify contact\n"+
          "Enter 6 To Exit\n------------------------")
    choice = input("Enter your choice: ") 
    
    if choice == "1":
        file1 = open(file_name, "r+")
        file_contents = file1.read()
        if len(file_contents) == 0:
            print("Phone Book is empty")
        else:
            print (file_contents)
        file1.close
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        search_contact_record()
        ent = input("Press Enter to continue ...")
        show_main_menu()
    elif choice =="4":
        delete_contact_record()
        ent=input("Press Enter to continue ....") 
        show_main_menu()   
    elif choice=="5":
        modify_contact_record()
        ent=input("Press Enter to continue ....") 
        show_main_menu()
    elif choice== "6":
        print("Thanks for using my PhoneBook Program created by:"+"\nBeng 20 COE 1 Group 2 \n")
    else:
        print("Wrong choice, Please Enter [1 to 6]\n")
        ent = input("Press Enter to continue ...")
        show_main_menu()
        
def search_contact_record():
    ''' This function is used to searches a specific contact record '''
    search_name = input("Enter First name for Searching contact record: ")
    rem_name = search_name[1:]
    first_char = search_name[0]
    search_name = first_char.upper() + rem_name
    file1 = open(file_name, "r+")
    file_contents = file1.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Required Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )

def input_fname():
    ''' Converts first letter of your name  to Upper case '''
    fname = input("Enter First name ")
    rem_fname = fname[1:]
    first_char = fname[0]
    return first_char.upper() + rem_fname

def input_lname():
    ''' Converts first letter of  last name  to Upper case '''
    lname = input("Enter Last name ")
    rem_lname = lname[1:]
    first_char = lname[0]
    return first_char.upper() + rem_lname


def enter_contact_record():
    ''' It  collects contact info firstname, last name, email and phone '''
   
    first = input_fname()
    last = input_lname()
    phone = input('Enter Phone number : ')
    email = input('Enter E-mail : ')
    contact = ("[" + first + " " + last + ", "+  phone + ", " + email +  "]\n")
    file1 = open(file_name, "a")
    file1.write(contact)
    print( "This contact\n " + contact + "has been added successfully!")

def delete_contact_record():#to delete the contact
     search_name = input("Enter First name for Searching contact record: ")
     rem_name = search_name[1:]
     first_char = search_name[0]
     search_name = first_char.upper() + rem_name
     file1 = open(file_name, "r+")
     file_contents = file1.readlines()
     

     for line in file_contents:
       file_contents.remove()

        
           
def modify_contact_record():#the aim of this function is to modify the content of the written 
     search_name = input("Enter First name for Searching contact record: ")
     rem_name = search_name[1:]
     first_char = search_name[0]
     search_name = first_char.upper() + rem_name
     file1 = open(file_name, "r+")
     file_contents = file1.readlines()
     
     found = False   
     for line in file_contents:
        if search_name in line:
              first = input_fname()
              last = input_lname()
              phone = input('Enter Phone number : ')
              email = input('Enter E-mail : ')
              contact = ("[" + first + " " + last + ", " + phone + ", " + email +  "]\n")
        print((line).replace(line,contact))   
        file1=open(file_name,"r+")
        file1.write(contact)
        found=True
        break
      
show_main_menu()
