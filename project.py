#EXPENSE TRACKER

expenses = []  


def add_expense():
    category = input("Category (food, transport, bills, other): ").strip().lower()
    description = input("Description: ").strip()

    while True:
        try:
            amount = float(input("Amount: "))
            if amount <= 0:
                raise ValueError("amount must be greater than 0.")
            break
        except ValueError as error:
            print(f"Invalid amount: {error}")

    expenses.append({"category": category, "description": description, "amount": amount})
    print("Expense added.\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    print(f"\n{'No.':<5}{'Category':<12}{'Description':<20}{'Amount':>10}")
    print("-" * 47)
    for number, expense in enumerate(expenses, start=1):
        print(
            f"{number:<5}{expense['category']:<12}"
            f"{expense['description']:<20}{expense['amount']:>10.2f}"
        )
    print()


def summary_by_category():
    if not expenses:
        print("No expenses recorded yet.\n")
        return

    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\nTotals by category:")
    for category, total in totals.items():
        print(f"  {category.title():<12}{total:>10.2f}")
    print(f"  {'TOTAL':<12}{sum(totals.values()):>10.2f}\n")


def delete_expense():
    if not expenses:
        print("No expenses to delete.\n")
        return

    view_expenses()
    try:
        number = int(input("Enter the number of the expense to delete: "))
        if not 1 <= number <= len(expenses):
            raise IndexError
        removed = expenses.pop(number - 1)
        print(f"Removed: {removed['description']}\n")
    except ValueError:
        print("Please enter a whole number.\n")
    except IndexError:
        print("There is no expense with that number.\n")


def main():
    menu = {
        "1": add_expense,
        "2": view_expenses,
        "3": summary_by_category,
        "4": delete_expense,
    }

    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Summary by category")
        print("4. Delete expense")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        action = menu.get(choice)
        if action:
            action()
        else:
            print("Invalid option, please try again.\n")


if __name__ == "__main__":
    main()