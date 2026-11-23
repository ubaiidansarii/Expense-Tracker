
print("===== SMART BUDGET PLANNER =====")

income = float(input("Enter your monthly income: "))
budget = float(input("Enter your monthly budget: "))

total_expenses = 0

while True:

    print("\n1. Add Expense")
    print("2. Check Total Expenses")
    print("3. Check Remaining Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Invalid amount!")
            continue

        total_expenses = total_expenses + amount

        print("Expense added successfully!")

        if total_expenses > budget:
            print("Warning! Budget exceeded!")

    elif choice == "2":

        print("Total Expenses:", total_expenses)

    elif choice == "3":

        remaining = income - total_expenses

        print("Remaining Balance:", remaining)

    elif choice == "4":

        print("Thank you for using Smart Budget Planner!")
        break

    else:
        print("Invalid choice! Try again.")
        continue
