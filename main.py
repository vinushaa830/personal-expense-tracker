expenses = []

while True:

    print("\n===== PERSONAL EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        category = input("Enter category: ")
        amount = float(input("Enter amount: ₹"))

        expense = {
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        print("Expense added successfully!")

    elif choice == "2":

        print("\n----- YOUR EXPENSES -----")

        if len(expenses) == 0:
            print("No expenses found.")

        else:
            for expense in expenses:
                print(
                    expense["category"],
                    "₹",
                    expense["amount"]
                )

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total spending: ₹", total)

    elif choice == "4":

        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice!")