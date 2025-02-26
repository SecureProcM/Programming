balance = 500
print(f"initial balance in account:{balance}")

deposit = 150
balance += deposit
print(f"Deposit {deposit} eur to account, balance is now: {balance}")

withdrawl = 200
balance -= withdrawl
print(f"Deposit{deposit} eur to account, balance is now: {balance}")

fee_percentage = 10/ 100
fee = balance * fee_percentage
balance -= fee
print(f"Deducting{fee_percentage * 100}% of fees to the account final balance:{balance:.1f}")