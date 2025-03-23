class BankAcc:
    def __init__(self):
        self.__owner = "Demo owner"
        self.__balance = 0
        self.__transaction_count = 0


    # Getters and setters
    # owner
    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    # balance
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    # transaction_count
    def get_transaction_count(self):
        return self.__transaction_count

    def set_transaction_count(self, transaction_count):
        self.__transaction_count = transaction_count

# Creating object of BankAcc class
shabab_acc = BankAcc()

# owner
shabab_acc.set_owner("Shabab")
print(shabab_acc.get_owner())

# balance
shabab_acc.set_balance(1000)
print(shabab_acc.get_balance())

# transaction_count
shabab_acc.set_transaction_count(2)
print(shabab_acc.get_transaction_count())




