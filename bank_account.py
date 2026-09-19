class BankAccount:
    bankTitle = "Wells Fargo"

    _next_account_number = 1000

    def __init__(self, customer_name, current_balance, minimum_balance, routing_number="121000248"):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        self._account_number = BankAccount._next_account_number
        BankAccount._next_account_number += 1

        self.__routing_number = routing_number

    def deposit(self, deposit_amount):
        self.current_balance += deposit_amount

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.current_balance and self.current_balance - withdraw_amount < self.minimum_balance:
            print("Balance insufficient, cannot withdraw")
        else:
            self.current_balance -= withdraw_amount

    def get_routing_number(self):
        """Private members aren't directly accessible outside the class,
        so we expose a getter method instead."""
        return self.__routing_number

    def get_account_number(self):
        return self._account_number

    def print_customer_information(self):
        print("Customer Name: " + self.customer_name)
        print("Current Balance: " + str(self.current_balance))
        print("Bank Title: " + BankAccount.bankTitle)
        print("Minimum Balance: " + str(self.minimum_balance))
        print("Account Number: " + str(self._account_number))
        print("Routing Number: " + str(self.__routing_number))
