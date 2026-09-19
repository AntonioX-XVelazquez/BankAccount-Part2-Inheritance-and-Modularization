from savings_account import SavingsAccount
from checking_account import CheckingAccount


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main():

    print_section("Scenario 1: Opening two Savings Accounts")

    savings1 = SavingsAccount("Alice Johnson", 1000, 100, 0.03)
    savings2 = SavingsAccount("Brian Lee", 500, 50, 0.015)

    savings1.print_customer_information()
    print()
    savings2.print_customer_information()

    print_section("Scenario 2: Alice deposits $200, then earns interest")
    savings1.deposit(200)
    savings1.apply_interest()
    savings1.print_customer_information()

    print_section("Scenario 3: Opening two Checking Accounts")

    checking1 = CheckingAccount("Carla Diaz", 800, 0, transfer_limit=500)
    checking2 = CheckingAccount("David Kim", 150, 0, transfer_limit=300)

    checking1.print_customer_information()
    print()
    checking2.print_customer_information()

    print_section("Scenario 4: Carla opens a checking account and withdraws $200")
    checking1.withdraw(200)
    checking1.print_customer_information()

    print_section("Scenario 5: Carla tries to withdraw more than she has")
    checking1.withdraw(10000)

    print_section("Scenario 6: Carla transfers $150 to David (within limit)")
    checking1.transfer(150, checking2)
    print()
    checking1.print_customer_information()
    print()
    checking2.print_customer_information()

    print_section("Scenario 7: Carla attempts a transfer over her transfer limit")
    checking1.transfer(1000, checking2)

    print_section("Scenario 8: Accessing account/routing numbers")
    print(f"Carla's account number (protected, direct access): {checking1._account_number}")
    print(f"Carla's routing number (private, via getter): {checking1.get_routing_number()}")


if __name__ == "__main__":
    main()
