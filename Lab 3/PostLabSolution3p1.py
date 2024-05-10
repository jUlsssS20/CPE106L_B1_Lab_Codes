

import pickle
import random
from savingsaccount import SavingsAccount

class Bank:
    """This class represents a bank as a collection of savings accounts.
    An optional file name is also associated with the bank, to allow transfer of accounts to and
    from permanent file storage."""

    def __init__(self, file_name: str = None):
        """Creates a new dictionary to hold the accounts.
        If a file name is provided, loads the accounts from a file of pickled accounts."""
        self.accounts = {}
        self.file_name = file_name
        if file_name is not None:
            try:
                with open(file_name, 'rb') as file_obj:
                    while True:
                        try:
                            account = pickle.load(file_obj)
                            self.add(account)
                        except EOFError:
                            break
            except (pickle.UnpicklingError, IOError) as e:
                print(f"Error loading accounts from file: {e}")

    def __str__(self) -> str:
        """Returns the string representation of the bank."""
        sorted_list = sorted(self.accounts.values(), key=lambda account: account.getName())
        return "\n".join(map(str, sorted_list))

    def make_key(self, name: str, pin: str) -> str:
        """Returns a key for the account."""
        return f"{name}/{pin}"

    def add(self, account: SavingsAccount) -> None:
        """Adds the account to the bank."""
        key = self.make_key(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name: str, pin: str) -> SavingsAccount:
        """Removes the account from the bank and returns it, or None if the account does not exist."""
        key = self.make_key(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name: str, pin: str) -> SavingsAccount:
        """Returns the account from the bank, or returns None if the account does not exist."""
        key = self.make_key(name, pin)
        return self.accounts.get(key, None)

    def compute_interest(self) -> float:
        """Computes and returns the interest on all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.compute_interest()
        return total

    def save(self, file_name: str = None) -> None:
        """Saves pickled accounts to a file. The parameter allows the user to change file names."""
        if file_name is not None:
            self.file_name = file_name
        elif self.file_name is None:
            return
        with open(self.file_name, 'wb') as file_obj:
            for account in self.accounts.values():
                pickle.dump(account, file_obj)

def create_bank(num_accounts: int = 1) -> Bank:
    """Returns a new bank with the given number of accounts."""
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia", "Ken", "Jill", "Jack")
    bank = Bank()
    upper_pin = num_accounts + 1000
    for pin_number in range(1000, upper_pin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pin_number), balance))
    return bank

def test_account() -> None:
    """Test function for savings account."""
    account = SavingsAccount("Ken", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())

def main(number: int = 10, file_name: str = None) -> None:
    """Creates and prints a bank, either from
    the optional file name argument or from the optional
    number."""

    test_account()
    if file_name:
        bank = Bank(file_name)
    else:
        bank = create_bank(number)
    print(bank)

if __name__ == "__main__":
    main()