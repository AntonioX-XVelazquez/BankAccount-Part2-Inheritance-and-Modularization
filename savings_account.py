from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate, routing_number="121000248"):
        super().__init__(customer_name, current_balance, minimum_balance, routing_number)
        self.interest_rate = interest_rate  

    def apply_interest(self):
        interest_earned = self.current_balance * self.interest_rate
        self.current_balance += interest_earned
        print(f"Interest applied: ${interest_earned:.2f}")

    def print_customer_information(self):
        super().print_customer_information()
        print("Account Type: Savings")
        print(f"Interest Rate: {self.interest_rate * 100:.2f}%")
