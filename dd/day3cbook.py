# contacts = {}
# while True:
#     print("\n1.add contact")
#     print("2.search contact")
#     print("3.update contact")
#     print("4.delete contact")
#     print("5.sort contact")
#     print("6.exit")
#     choice=int(input("enter choice"))
#     if choice =="1":
#         name = input("enter name:")
#         phone = input("enter name:")
#         contacts[name] = phone
#         print("correct added")
#     elif choice == "2":
#         name = input("enter name")
#         if name in contacts:
#              print("phone number:",contacts[name])
#         else:
#             print("contacts not found")
#     elif choice == "3":
#         name =input("name")
#         if name in contacts:
#             new_phone =input("new number:")
#             contacts[name] = new_phone
#             print("contact updatrd")
#         else:
#             print("çontacts not found")
#     elif choice == "4":
#         name = input("enter name")
#         if name in contacts:
#             del contacts[name]
#             print("contact deleted")
#         else:
#            print("contacts not found")
#     elif choice == "5":
#         print("\n sorted contacts")
#         for name in sorted(contacts):
#             print(name,":",contacts[name])
#     elif choice == "6":
#          print("exit")
#          break
#     else:
#         print("invalied choice")
        
contacts = {}
while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Sort contacts")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter number: ")
        contacts[name] = phone
        print("Contact added successfully")

    elif choice == "2":
        name = input("Enter name: ")
        if name in contacts:
            print("Phone number:", contacts[name])
        else:
            print("Contact not found")

    elif choice == "3":
        name = input("Enter name: ")
        if name in contacts:
            newphone = input("Enter new number: ")
            contacts[name] = newphone
            print("Contact updated!")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found")

    elif choice == "5":
        print("\nSorted Contacts:")
        for name in sorted(contacts):
            print(name, ":", contacts[name])

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")