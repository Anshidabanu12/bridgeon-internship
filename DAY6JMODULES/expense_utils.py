import json
FILE_NAME="expenses.json"

def load_expences():
    try:
        with open(FILE_NAME,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]
    
def save_expenses(expenses):
    with open(FILE_NAME,"w") as f:
        json.dump(expenses,f,indent=2)

def add_expense(category,amount):
    expenses=load_expences()

    expence={
        "category":category,
        "amount":amount
    }
    expenses.append(expence)
    save_expenses(expenses)

    print("Expense add successfully")

def get_summary():
    expenses=load_expences()

    summary={}

    for expense in expenses:
        category=expense["category"]
        amount=expense["amount"]

        if category in summary:
            summary[category]+=amount
        else:
            summary[category]=amount

        print("\n Expense summary")
        for category,total in summary.items():
            print(f"{category}:{total}")

def view_all():
    expenses=load_expences()

    if not expenses:
        print("No expenses found")
        return
    
    print("\nAll Expenses")
    for expense in expenses:
        print(f"category:{expense['category']} amount:{expense['amount']}")
