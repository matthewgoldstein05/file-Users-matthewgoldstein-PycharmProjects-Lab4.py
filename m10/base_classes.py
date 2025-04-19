class Account:
    def __init__(self):
        self.balance = 0

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Invalid amount")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount")


class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


class Fraction:
    def __init__(self, numerator, denominator):
        def gcd(a, b):
            if b == a:
                return a
            if b > a:
                return gcd(b, a)
            return gcd(a - b, b)

        gcd = gcd(numerator, denominator)
        if gcd != 1:
            numerator //= gcd
            denominator //= gcd
        self.num = numerator
        self.den = denominator

    def get_numerator(self):
        return self.num

    def get_denominator(self):
        return self.den

    def multiply(self, other):
        numerator = self.get_numerator() * other.get_numerator()
        denominator = self.get_denominator() * other.get_denominator()
        return type(self)(numerator, denominator)  # If self is a child class, create that instead

    def add(self, other):
        if self.get_denominator() == other.get_denominator():
            numerator = self.get_numerator() + other.get_numerator()
            denominator = self.get_denominator()
        else:
            numerator = self.get_numerator() * other.get_denominator() + other.get_numerator() * self.get_denominator()
            denominator = self.get_denominator() * other.get_denominator()
        return type(self)(numerator, denominator)  # If self is a child class, create that instead