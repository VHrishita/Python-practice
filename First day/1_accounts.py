balance = 5000

print("1.Deposit  2.Withdraw  3.Check Balance")
choice = int(input("Enter choice: "))

match choice:
    case 1:
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Balance:", balance)

    case 2:
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Balance:", balance)
        else:
            print("Insufficient balance")

    case 3:
        print("Balance:", balance)

    case _:
        print("Invalid choice")