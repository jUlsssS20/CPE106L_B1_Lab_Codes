# savingsaccount.py

class SavingsAccount:
    """This class represents a savings account
    with the owner's name, PIN, and balance."""

    RATE = 0.02    # Single rate for all accounts

    def __init__(self, name: str, pin: str, balance: float = 0.0):
        """Initializes a SavingsAccount object."""
        self._name = name
        self._pin = pin
        self._balance = balance

    @property
    def name(self) -> str:
        """Returns the account owner's name."""
        return self._name

    @property
    def pin(self) -> str:
        """Returns the account PIN."""
        return self._pin

    @property
    def balance(self) -> float:
        """Returns the current balance."""
        return self._balance

    def __str__(self) -> str:
        """Returns the string representation of the account."""
        result =  'Name:    ' + self.name + '\n' 
        result += 'PIN:     ' + self.pin + '\n' 
        result += 'Balance: ' + str(self.balance)
        return result

    def deposit(self, amount: float) -> None:
        """Deposits the given amount into the account."""
        if amount < 0:
            raise ValueError("Amount must be >= 0")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraws the given amount from the account."""
        if amount < 0:
            raise ValueError("Amount must be >= 0")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def compute_interest(self) -> float:
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest