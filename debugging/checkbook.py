class Checkbook:
    """
    A simple checkbook class that allows deposits, withdrawals,
    and balance inquiries.
    """

    def __init__(self):
        """
        Initialize a new Checkbook instance with a starting balance of $0.00.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposit a specified amount into the checkbook.

        Parameters:
            amount (float): The amount of money to deposit.

        Behavior:
            - Adds the amount to the current balance.
            - Prints confirmation and updated balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the checkbook if sufficient funds exist.

        Parameters:
            amount (float): The amount of money to withdraw.

        Behavior:
            - Checks if the balance is sufficient.
            - If not, prints an error message.
            - Otherwise, subtracts the amount and prints confirmation.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Display the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Main program loop that allows the user to interact with the Checkbook.

    Available commands:
        - deposit : Add money to the balance
        - withdraw: Remove money from the balance
        - balance : Display current balance
        - exit    : Exit the program
    """
    cb = Checkbook()

    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        )

        if action.lower() == 'exit':
            break

        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)

        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)

        elif action.lower() == 'balance':
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
