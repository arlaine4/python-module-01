import sys


class Account:

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def __str__(self):
        return f'Account name : {self.name}\n - amount : {self.value}'


class Bank:
    """The Bank"""
    def __init__(self):
        self.account = []

    def check_account_not_in_accounts(self, account):
        for acc in self.account:
            if acc.name == account.name:
                return False
        return True

    def add(self, account):
        if isinstance(account, Account) and self.check_account_not_in_accounts(account):
            self.account.append(account)
        else:
            print(f'Invalid account {account.name}, not adding it to the bank')

    def check_and_return_account_idx(self, account_name):
        """
        Checking an account id in self.account list
        - looping over accounts instances in self.account
          and comparing accounts names with the current account name being checked
        """
        for i, account in enumerate(self.account):
            if account.name == account_name:
                return i
        return False

    def transfer(self, origin, dest, amount):
        # Checking origin parameter validity
        if not origin or type(origin) not in [str, int]:
            sys.exit('Invalid account origin')
        # Getting id of origin account from it's name if the account is valid
        if type(origin) is str:
            origin = self.check_and_return_account_idx(origin)
        # Checking dest parameter validity
        if not dest or type(dest) not in [str, int]:
            sys.exit('Invalid account dest')
        # Getting id of dest account from it's name if the account is valid
        if type(dest) is str:
            dest = self.check_and_return_account_idx(dest)
        # Checking amount parameter validity
        if not float or type(amount) is not float or amount < 0:
            sys.exit('Invalid amount')
        # Transfer
        if origin and dest:
            if origin.value >= amount:
                dest.transfer(amount)
                return True
            else:
                print('Not enough money on origin for transfer')
                return False

    def fix_account(self, account):
        pass

    def __str__(self):
        to_ret = '\n'
        for i, account in enumerate(self.account):
            if i == len(self.account) - 1:
                to_ret += account.__str__() + '\n'
            else:
                to_ret += account.__str__() + '\n\n'
        return to_ret


if __name__ == "__main__":
    bank1 = Bank()
    account1 = Account('test')
    bank1.add(account1)
    account2 = Account('test')
    bank1.add(account2)
    print(bank1)