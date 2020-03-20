import datetime
import pytz


class Account:
    """ Simple account class with balance """

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount, self.balance))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount, self.balance))
        else:
            print("The amount must be greater than zero and no more then your account balance")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount, self.balance in self.transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {})".format(amount, tran_type, date, date.astimezone()))
            print("   Available balance is {}".format(self.balance))


if __name__ == '__main__':
    kim = Account("Kim", 0)
    kim.show_balance()

    kim.deposit(1000)
    # kim.show_balance()
    kim.withdraw(500)
    # kim.show_balance()

    kim.withdraw(2000)

    kim.show_transactions()

    jaydeep = Account("Jaydeep", 800)
    jaydeep.deposit(100)
    jaydeep.withdraw(200)
    jaydeep.show_transactions()
