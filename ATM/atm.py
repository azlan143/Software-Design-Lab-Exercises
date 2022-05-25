from breezypythongui import EasyFrame
from bank import Bank, createBank

def main(fileName = None):
     """Creates the bank with the optional file name,
     wraps the window around it, and opens the window.
     Saves the bank when the window closes."""
     if not fileName:
        bank = createBank(5)
     else:
        bank = Bank(fileName)
     print(bank) # For testing only
     atm = ATM(bank)
     atm.mainloop()
     # Could save the bank to a file here.

class ATM(EasyFrame):
     """Represents an ATM window.
     The window tracks the bank and the current account.
     The current account is None at startup and logout.
     """
     error_attempts = 3
     def __init__(self, bank):
        """Initialize the window and establish
         the data model."""
        EasyFrame.__init__(self, title = "ATM")
        # Create references to the data model.
        self.bank = bank
        self.account = None
        # Create and add the widgets to the window."""
        self.nameLabel = self.addLabel(row=0, column=0,
                                       text="Name")
        self.pinLabel = self.addLabel(row=1, column=0,
                                      text="PIN")
        self.amountLabel = self.addLabel(row=2, column=0,
                                         text="Amount")
        self.statusLabel = self.addLabel(row=3, column=0,
                                         text="Status")
        self.nameField = self.addTextField(row=0, column=1,
                                           text="")
        self.pinField = self.addTextField(row=1, column=1,
                                          text="")
        self.amountField = self.addFloatField(row=2, column=1,
                                              value=0.0)
        self.statusField = self.addTextField(row=3, column=1,
                                             text="Welcome to the Bank!",
                                             state="readonly")
        self.balanceButton = self.addButton(row=0, column=2,
                                            text="Balance",
                                            command=self.getBalance,
                                            state="disabled")
        self.depositButton = self.addButton(row=1, column=2,
                                            text="Deposit",
                                            command=self.deposit,
                                            state="disabled")
        self.withdrawButton = self.addButton(row=2, column=2,
                                             text="Withdraw",
                                             command=self.withdraw,
                                             state="disabled")
        self.loginButton = self.addButton(row=3, column=2,
                                          text="Login",
                                          command=self.login)
        self.counter = 0

     def login(self):
        """Attempts to login the customer. If successful,
        enables the buttons, including logout."""
        name = self.nameField.getText()
        pin = self.pinField.getText()
        self.account = self.bank.get(name, pin)
        if self.account:
            self.statusField.setText("Hello, " + name + "!")
            self.balanceButton["state"] = "normal"
            self.depositButton["state"] = "normal"
            self.withdrawButton["state"] = "normal"
            self.loginButton["text"] = "Logout"
            self.loginButton["command"] = self.logout
        else:
            self.statusField.setText("Name or pin not found!")
            self.counter += 1
            if self.counter == ATM.error_attempts:
                self.loginButton["state"] = "disable"
                self.prompt = self.prompterBox(title="Error",
                                               promptString="Too many failed attempts(Unable to login)\nCalling the police...",
                                               fieldWidth=20)

     def logout(self):
         """Logs the customer out, clears the fields,
         disables the buttons, and enables login."""
         self.account = None
         self.nameField.setText("")
         self.pinField.setText("")
         self.amountField.setNumber(0.0)
         self.statusField.setText("Welcome to the Bank!")
         self.balanceButton["state"] = "disabled"
         self.depositButton["state"] = "disabled"
         self.withdrawButton["state"] = "disabled"
         self.loginButton["text"] = "Login"
         self.loginButton["command"] = self.login

     def getBalance(self):
         """Displays the current balance in the
         status field."""
         balance = self.account.getBalance()
         self.statusField.setText("Balance: $" + str(balance))

     def deposit(self):
         """Attempts a deposit. If not successful, displays
         error message in statusfield; otherwise, announces
         success."""
         amount = self.amountField.getNumber()
         message = self.account.deposit(amount)
         if not message:
             self.statusField.setText("Deposit successful")
         else:
             self.statusField.setText(message)

     def withdraw(self):
         """Attempts a withdrawal. If not successful,
         displays error message in statusfield;
         otherwise, announces success."""
         amount = self.amountField.getNumber()
         message = self.account.withdraw(amount)
         if message:  # Check for an error message
             self.statusField.setText(message)
         else:
             self.statusField.setText("Withdrawal successful!")

if __name__ == "__main__":
    main()