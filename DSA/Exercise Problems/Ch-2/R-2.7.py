class CreditCard():
    def __init__(self, customer, bank, acnt, limit, balance=0):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = balance

    def get_customer(self):
        return self._customer

    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    def charge(self, price):
        try:
            if price + self._balance > self._limit:
                return False
            else:
                return True
        except (TypeError):
            print('Please enter a numeric value.')
            return False

    def make_payment(self, amount):
        try:
            self._balance -= amount
        except (TypeError):
            print('Please enter a numeric value.')
            return False

