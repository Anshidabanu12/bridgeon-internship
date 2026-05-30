contacts = {}
while True:
    choice=int("enter your contact")
    print("\n1.add contact")
    print("2.search contact")
    print("3.update contact")
    print("4.delete contact")
    print("5.sort contact")
    print("6.exit")
    choice=int(input("enter choice"))
    if choice == 1:
        name = input("enter name:")
        phone = input("enter name:")
        contacts[name] = phone
        print("correct added")
    elif choice == 2:
        name = input("enter name")
        print(contacts.get(name))
    elif choice == 3:
        name =input("name")
        if name in contacts:
            new_phone =input("new number:")
            contacts[name] = new_phone
            print("contact updatrd")
    elif choice == 4:
        name = input("enter name")
        if name in contacts:
            del contacts[name]
            print("contact deleted")
    elif choice == 5:
        for i in sorted(contacts):
            print(f"{i}:{contacts[i]}")
    elif choice ==6:
         print("exit")
         break
    else:
        print("invalied choice")
        
    