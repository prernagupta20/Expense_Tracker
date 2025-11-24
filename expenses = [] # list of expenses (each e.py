expenses = [] 

print("Welcome to Expense Tracker:")

while True:
    print("\n=== MENU ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Search Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Please Enter Your Choice: ")

    # 1. ADD EXPENSE
    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    # 2. VIEW ALL EXPENSES
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses added yet.")
        else:
            print("\n=== ALL EXPENSES ===")
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, "
                      f"Description: {expense['description']}, Amount: ₹{expense['amount']}")

    # 3. VIEW TOTAL SPENDING
    elif choice == "3":
        total = sum(exp["amount"] for exp in expenses)
        print(f"Total Spending: ₹{total}")

    # 4. SEARCH EXPENSE
    elif choice == "4":
        keyword = input("Enter date/category/description to search: ").lower()
        found = False

        for expense in expenses:
            if (keyword in expense["date"].lower() or
                keyword in expense["category"].lower() or
                keyword in expense["description"].lower()):
                print(f"Found: {expense}")
                found = True

        if not found:
            print("No matching expense found.")

    # 5. DELETE EXPENSE
    elif choice == "5":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            for idx, expense in enumerate(expenses, start=1):
                print(f"{idx}. {expense}")

            delete_index = int(input("Enter the number of expense to delete: "))
            if 1 <= delete_index <= len(expenses):
                deleted = expenses.pop(delete_index - 1)
                print(f"Deleted: {deleted}")
            else:
                print("Invalid index.")

    # 6. EXIT
    elif choice == "6":
        print("Exiting Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
