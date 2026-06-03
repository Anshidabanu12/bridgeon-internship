import json
FILE_NAME = "expenses.json"
def load_expense():
    try:
        with open(FILE_NAME,"r") as f:
            return json.load(f)
    except FileNotFoundError:
      return []

def save_expenses(expenses):
    with open(FILE_NAME,"W") as f:
        json.dump(expenses, f, indent=2)

def add_expenses(category,amount):
   expenses = load_expense()

   expense = {
       "category":category,
       "amount":amount
   }

   expenses.append(expenses)
   save_expenses(expenses) 
   print("expense added successfully")
    
def get_summery():
   expenses = load_expense()

   summery = {}
   for expenses in expenses:
    category = expenses["category"]
    amount = expenses["amount"]

    if category in summery :
       summery[category] += amount
    else:
       summery[category] = amount

    print("\nexpenses summery")
    for category, total in summery.item():
       print(f"{category}:{total}")


def view_all():
   add_expenses =  load_expense()

   if not expenses:
      print("no expenses found")
      return 
   
   print("\nall expenses")
   for expenses in expenses:
      print(f"category:{expenses['category']},amount:{expenses['amount']}")