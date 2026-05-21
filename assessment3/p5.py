# 5. ATM Withdrawal Check

balance = 5000
amount = int(input("Enter withdrawal amount: "))

if amount <= balance:
    print("Withdrawal successful")
else:
    print("Insufficient balance")