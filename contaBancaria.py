class AlertaErro(Exception):
    pass

class Account:
    def __init__(self, number:int, holder:str, balance:float, withdraw_limit:float):
        if number <= 0:
            raise AlertaErro("Number account must be greater than zero")

        if not holder.strip():
            raise AlertaErro("Account holder cannot be empty")

        if(balance < 0):
            raise AlertaErro("Initial balance cannot be negative")

        if(withdraw_limit < 0):
            raise AlertaErro("Withdraw limit cannot be negative")

        self._number = number
        self._holder = holder
        self._balance = balance
        self._withdraw_limit = withdraw_limit

    @property
    def number(self):
        return self._number
    
    @property
    def holder(self):
        return self._holder
    
    @property
    def balance(self):
        return self._balance
    
    @property
    def withdraw_limit(self):
        return self._withdraw_limit

    def deposit(self, amount:float) -> None:
        if amount <= 0:
            raise AlertaErro("Deposit error: the amount must be greater than zero")
        self._balance += amount

    def withdraw(self, amount:float) -> None:
        if amount <= 0:
            raise AlertaErro("Withdraw error: amount must be greater than zero")
        if amount > self._withdraw_limit:
            raise AlertaErro("Withdraw error: The amount exceeds withdraw limit")
        if amount > self._balance:
            raise AlertaErro("Withdraw error: Not enough balance")
        self._balance -= amount

print("Enter account data")

try:
    number = int(input("Number: "))
    holder = input("Holder: ")
    initial_balance = float(input("Initial balance: "))
    withdraw_limit = float(input("Withdraw limit: "))
    acc = Account(number, holder, initial_balance, withdraw_limit)
except (ValueError, AlertaErro) as e:
    print(e)
else:   
    amount = float(input("\nEnter amount for withdraw: "))

    try:
        acc.withdraw(amount)
    except AlertaErro as e:
        print(e)
    else:
        print(f"New balance: {acc.balance:.2f}")