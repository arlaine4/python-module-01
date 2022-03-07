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
        elif not isinstance(account, Account):
            print(f'{account} is not an instance of Account class, not adding it to the bank')
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
        """
        Verify Account's instance attributes
        """
        found_extras = {'b': True, 'zip': False, 'addr': False, 'name': False, 'id': False, 'value': False}
        for attr in account.__dict__.keys():
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
        print(found_extras)
        if False in list(found_extras.values()):
            if found_extras['zip'] is True and found_extras['addr'] is False:
                found_extras['addr'] = True
            if found_extras['addr'] is True and found_extras['zip'] is False:
                found_extras['zip'] = True
            if False not in list(found_extras.values()):
                return True
            if mode_fix:
                return found_extras
            return False
        return True

    def verify_corrupted_account(self, accounts_lst):
        """
        Verify if dest or origin accounts are corrupted before making a transfer
        """
        for account_idx in accounts_lst:
            if not Bank.verify_valid_attributes_account(self.account[account_idx]):
                print('corrupted ', self.account[account_idx].name)
                return True
        return False

    def fix_account(self, account):
        # Getting account index in accounts list by it's name
        account = self.check_and_return_account_idx(account)
        if account is False:
            return False
        # Getting attributes list and keeping only the ones that needs fixing
        infos_to_fix = Bank.verify_valid_attributes_account(self.account[account], mode_fix=True)
        if type(infos_to_fix) is bool and len(list(self.account[account].__dict__.keys())) % 2 != 0:
            print(f"Account {self.account[account].name} doesn't need fixing")
            return False
        if type(infos_to_fix) is not bool:
            final_infos = {}
            for key in infos_to_fix.keys():
                if infos_to_fix[key] is False:
                    final_infos[key] = False
            # Fixing attributes
            try:
                for key in final_infos.keys():
                    if key == 'zip':
                        self.account[account].__dict__[key] = '100-085'
                    if key == 'value':
                        self.account[account].__dict__['value'] = 0
                    if key == 'b':
                        # Getting index of attribute starting with b in order to delete it
                        attr_idx = int([i for i in range(len(self.account[account].__dict__.keys())) if
                                        list(self.account[account].__dict__.keys())[i].startswith('b')][0])
                        key_to_del = list(self.account[account].__dict__.keys())[attr_idx]
                        delattr(self.account[account], key_to_del)
            except:
                return False
        # Adding a random attribute to make attributes count odd
        if len(list(self.account[account].__dict__.keys())) % 2 == 0:
            self.account[account].random_attribute = None
        print(f'Account {self.account[account].name} fixed')
        return True

    def __str__(self):
        to_ret = '\n'
        for i, account in enumerate(self.account):
            if i == len(self.account) - 1:
                to_ret += account.__str__() + '\n'
            else:
                to_ret += account.__str__() + '\n\n'
        return to_ret
