from bank_account import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, transfer_limit, routing_number="121000248"):
        super().__init__(customer_name, current_balance, minimum_balance, routing_number)
        self.transfer_limit = transfer_limit  

    def transfer(self, amount, recipient_account):

        if amount > self.transfer_limit:
            print(f"Transfer failed: ${amount} exceeds the transfer limit of ${self.transfer_limit}")
            return

        if amount > self.current_balance and self.current_balance - amount < self.minimum_balance:
            print("Transfer failed: insufficient balance")
            return

        self.withdraw(amount)
        recipient_account.deposit(amount)
        print(f"Transferred ${amount} to account #{recipient_account.get_account_number()}")

    def print_customer_information(self):
        super().print_customer_information()
        print("Account Type: Checking")
        print(f"Transfer Limit: ${self.transfer_limit}")
