class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Внесено {amount}. Баланс: {self.__balance}"
        return "Сумма должна быть положительной."

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return f"Снято {amount}. Баланс: {self.__balance}"
        return "Недостаточно средств."

    def get_balance(self):
        return self.__balance

account = BankAccount("Александр Март")
print(account.deposit(1000))
print(account.withdraw(500))
print(account.get_balance())