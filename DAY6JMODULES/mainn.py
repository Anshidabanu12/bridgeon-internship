# from expense_utils import add_expenses, get_summery, view_all
# while True:
#     print("\n1. add expense :")
#     print("2. summery :" )
#     print("3. view all :")
#     print("4. exit :")
#     choice = input("enter choice :")
#     if choice == "1":
#         category = input("énter category :")
#         amount = float(input("enter amount :"))

#         add_expenses(category,amount)
#     elif choice == "2":
#         get_summery()
#     elif choice == "3":
#         view_all
#     elif choice == "4":
#         print("goodbye!")
#         break
#     else:
#         print("invalid choice")
from expense_utils import add_expense,get_summary,view_all
while True:
    print("\n1. Add Expense")
    print("2.Summary")
    print("3.View All")
    print("4.Exit")

    choice=input("Enter choice:")

    if choice=="1":
        category=input("Enter category:")
        amount=float(input("Enter amount:"))

        add_expense(category,amount)

    elif choice=="2":
        get_summary()
    elif choice=="3":
        view_all()
    elif choice=="4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")