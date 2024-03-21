class BankAccount:
    def __init__(self, account_number, name):
        self.__account_number = account_number
        self.__name = name

    @property
    def account_number(self):
        return self.__account_number

    @account_number.setter
    def account_number(self, new_account_number):
        self.__account_number = new_account_number

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

account = BankAccount("1234567890", "John Doe")

print("Account Number:", account.account_number)
print("Name:", account.name)

account.account_number = "9876543210"
account.name = "Jane Smith"

print("\nAfter Update:")
print("Account Number:", account.account_number)
print("Name:", account.name)
