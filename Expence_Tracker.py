import datetime

def add_expense():
    try:
        with open("expenses.txt", "a") as file:
            file.write(f"{datetime.date.today()}, {input('Amount: ')}, {input('Category: ')}, {input('Description: ')}\n")
        print("Expense added!\n")
    except:
        print("Invalid input!\n")

def view_expenses():
    try:
        with open("expenses.txt") as file:
            expenses = file.readlines()
            print("Date          Amount  Category       Description\n" + "-"*50)
            print("".join(expenses) if expenses else "No expenses recorded yet.\n")
    except FileNotFoundError:
        print("No expenses found.\n")

def total_by_category():
    try:
        with open("expenses.txt") as file:
            totals = {}
            for line in file:
                _, amount, category, _ = line.strip().split(", ")
                totals[category] = totals.get(category, 0) + float(amount)
            print("\n".join(f"{cat}: ${total:.2f}" for cat, total in totals.items()) if totals else "No expenses recorded yet.\n")
    except FileNotFoundError:
        print("No expenses found.\n")

while True:
    choice = input("1. Add Expense  2. View Expenses  3. Total by Category  4. Exit\nChoose: ")
    {"1": add_expense, "2": view_expenses, "3": total_by_category, "4": exit}.get(choice, lambda: print("Invalid choice!\n"))()
