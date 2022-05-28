from savingsaccount import SavingsAccount
import pickle
import random

class Bank(object):
    def __init__(self, fileName=None):
        """Creates a new dictionary to hold the accounts.
        If a filename is provided, loads the accounts from
        a file of pickled accounts."""
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, "rb")
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except EOFError:
                    fileObj.close()
                    break

    def __str__(self):
         """Return the string rep of the entire bank."""
         return '\n'.join(map(str, self.accounts.values()))

    def makeKey(self, name, pin):
        """Makes and returns a key from name and pin."""
        return name + "/" + pin

    def add(self, account):
        """Inserts an account with name and pin as a key."""
        key = self.makeKey(account.getName(),
                           account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes an account with name and pin as a key."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns an account with name and pin as a key
        or None if not found."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes interest for each account and
            returns the total."""
        total = 0.0
        for account in self.accounts.values():
            total += account.computelnterest()
        return total

    def save(self, fileName=None):
        """Saves pickled accounts to a file. The parameter
        allows the user to change filenames."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, "wb")
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

def createBank(numAccounts = 1):
    """Returns a new bank with the given number of
    accounts."""
    names = ("Brandon", "Molly", "Elena", "Mark", "Tricia",
             "Ken", "Jill", "Jack")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank