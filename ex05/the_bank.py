import sys


class Account:
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

    def __str__(self):
        if 'value' in self.__dict__.keys():
            return f'Account name : {self.name}\n - amount : {self.value}\n'
        else:
            return f'Account name : {self.name}\n - amount : 0\n'


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
            print('Invalid account origin')
            return False
        # Getting id of origin account from it's name if the account is valid
        if type(origin) is str:
            origin = self.check_and_return_account_idx(origin)
            if type(origin) is not int:
                print('Invalid account origin')
                return False
        # Checking dest parameter validity
        if not dest or type(dest) not in [str, int]:
            print('Invalid account dest')
            return False
        # Getting id of dest account from it's name if the account is valid
        if type(dest) is str:
            dest = self.check_and_return_account_idx(dest)
            if type(dest) is not int:
                print('Invalid dest account')
                return False
        # Checking amount parameter validity
        if type(amount) not in [int, float] or amount < 0:
            print('Invalid amount')
            return False
        # Transfer
        try:
            if self.verify_corrupted_account([origin, dest]):
                print("One or more corrupted account, not proceeding with the transfer")
                return False
            if self.account[origin].value >= amount:
                self.account[dest].transfer(amount)
                self.account[origin].value -= amount
                print(f'Successful transfer from {self.account[origin].name} to {self.account[dest].name} of {amount}')
                return True
            else:
                print('Not enough money on origin for transfer')
                return False
        except AttributeError:
            print("One or more corrupted account, not proceeding with the transfer")
            return False

    @classmethod
    def verify_valid_attributes_account(cls, account, mode_fix=False):
        found_extras = {'b': True, 'zip': False, 'addr': False, 'name': False, 'id': False, 'value': False,
                        'odd_attributes_number': len(dir(account)) % 2 == 0}
        for attr in dir(account):
            if attr.startswith('b'):
                found_extras['b'] = False
            elif attr.startswith('zip'):
                found_extras['zip'] = True
            elif attr.startswith('addr'):
                found_extras['addr'] = True
            elif attr == 'name':
                found_extras['name'] = True
            elif attr == 'id':
                found_extras['id'] = True
            elif attr == 'value':
                found_extras['value'] = True
        if False in list(found_extras.values())[:-1]:
            if mode_fix:
                return found_extras
            return False
        return True

    def verify_corrupted_account(self, accounts_lst):
        for account_idx in accounts_lst:
            if not Bank.verify_valid_attributes_account(self.account[account_idx]):
                return True
        return False

    def fix_account(self, account):
        account = self.check_and_return_account_idx(account)
        if account is False:
            return False
        infos_to_fix = Bank.verify_valid_attributes_account(self.account[account], mode_fix=True)
        final_infos = {}
        for key in infos_to_fix.keys():
            if infos_to_fix[key] is False:
                final_infos[key] = False
        try:
            for key in final_infos.keys():
                if key == 'odd_attributes_number':
                    continue
                if key in ['zip', 'addr', 'value']:
                    self.account[account].__dict__[key] = 0
                if key == 'b':
                    attr_idx = int([i for i in range(len(self.account[account].__dict__.keys())) if
                                    list(self.account[account].__dict__.keys())[i].startswith('b')][0])
                    key_to_del = list(self.account[account].__dict__.keys())[attr_idx]
                    delattr(self.account[account], key_to_del)
            if 'odd_attributes_number' in final_infos and len(dir(self.account[account])) % 2 == 0:
                self.account[account].random_attribute = None
            print(f'Account {self.account[account].name} fixed')
            return True
        except:
            return False

    def __str__(self):
        to_ret = '\n'
        for i, account in enumerate(self.account):
            if i == len(self.account) - 1:
                to_ret += account.__str__() + '\n'
            else:
                to_ret += account.__str__() + '\n\n'
        return to_ret


if __name__ == "__main__":
    # PROBLEME WITH ADD_ATTRIBUTES_NUMBER IN
    bank1 = Bank()
    account1 = Account('test', value=0)
    account2 = Account('test2', bonsoir='ok')
    account_found = Account('test3', value=1000)
    bank1.add(account1)
    bank1.add(account2)
    #bank1.transfer('test2', 'test', 200)
    bank1.fix_account('test2')
    #bank1.transfer('test2', 'test', 200)
    bank1.fix_account('test')
    bank1.transfer('test2', 'test', 200)
    bank1.add(account_found)
    bank1.transfer('test3', 'test2', 200)
    bank1.fix_account('test3')
    bank1.transfer('test3', 'test2', 200)
    bank1.transfer('test2', 'test', 200)
    print(bank1)
    #bank1.transfer('test3', 'test2', 200)
    #bank1.add(account_found)
    #bank1.transfer('test3', 'test2', 200)
    #bank1.fix_account('test3')
    #bank1.transfer('test3', 'test2', 200)
