contacts = {}
def menu():
    print(' 1.ADD NAME\n 2.REMOVE CONTACT \n 3.UPDATE CONTACT\n 4.SEARCH CONTACT\n 5.EXIT')
def add_contact(name,phone):
    num = 1
    contacts[name] = phone
    print(f" Added {name} with phone number: {phone}")
def  remove_contact (name) :
    if name in contacts:
        del contacts[name]
        print(f"Removed contact{name}")

    else:
        print(f"{name}not found")

def update_contact(name,phone):
    if name in contacts:
        contacts[name] = phone
        print(f"Updated {name} with new phone number{phone}")
    else:
        print(f"{name}not found")
         
def search_contact(name):
    if name in contacts:
       print(f"{name}:{contacts[name]}")
    else:
        print(f"{name}not found")
def main():
    

    choice = 99

    while choice != 5:
        menu()
        choice = int(input('Enter the choice from menu'))

        if choice == 1:
            name = input('Please enter the name you have')
            phone = int(input('Please enter the contact number you have'))
            add_contact(name,phone)
            
        elif choice == 2:
           name = input('Please enter the name on your contacts')
           remove_contact(name)
            
        elif choice == 3:
            name = input('Please enter the name you have')
            phone = int(input('Please enter the contact number you want to change'))
            update_contact(name,phone)
            
        elif choice == 4:
            name = input('Please enter the name you have')
            phone = int(input('Please enter the contact number you want to change'))
            search_contact(name)     
    print('Press enter to exit')
    if choice == 99:
        print('invalid input')
        exit()
main()
