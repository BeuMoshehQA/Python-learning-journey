data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_transactions(transactions):
  for transaction in transactions:
    amount, statement = transaction
    print(f"${amount} - {statement}")

print_transactions(data)

def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposited = sum(deposits)
  print(f"Total deposited: {total_deposited}")
  withdrawals = [transaction[0] for transaction in transactions if transaction [0] < 0]
  total_withdrawals = sum(withdrawals)
  print(f"Total withdrawals: {total_withdrawals}")
  balance = (total_deposited + total_withdrawals)
  print(balance)

def analyze_transactions(transactions):
  transactions.sort()
  largest_withdrawal = transactions[0]
  largest_deposit = transactions[-1]
  print(f"The largest withdrawal is: {largest_withdrawal}")
  print(f"The largest deposit is: {largest_deposit}")
  deposits = [transaction[0] for transaction in transactions if transaction[0] >= 0]
  total_deposit = sum(deposits)
  average_deposit = total_deposit/len(deposits) if deposits else 0
  print(average_deposit)
  withdrawals = [transaction[0] for transaction in transactions if transaction [0] < 0]
  total_withdrawals = sum(withdrawals)
  average_withdrawals = total_withdrawals/len(withdrawals) if withdrawals else 0
  print(average_withdrawals)

while True:
    print("\nChoose an option:")
    print("Type 'print' to see the transaction summary.")
    print("Type 'analyze' to analyze the transactions.")
    print("Type 'stop' to exit the program.")
    choice = input()
    if choice == "print":
      print_summary(data)
    elif choice == "analyze":
      analyze_transactions(data)
    elif choice == "stop":
      break
    else:
      print("invalid choice")