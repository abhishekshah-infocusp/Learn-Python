class BankAccount:

    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if amount < 0:
            return False
        
        if self.balance >= amount:
            self.balance -= amount
            return True

        return False

    def deposit(self, amount):
        self.balance += amount
        return True

def test_insufficient_deposit():
    # Arrange
    a = BankAccount(1)
    a.deposit(100)

    # Act
    outcome = a.withdraw(200)

    # Assert
    assert outcome == False

def test_negative_deposit():
    # Arrange
    a = BankAccount(1)
    a.deposit(100)

    # Act
    outcome = a.withdraw(-200)

    # Assert
    assert outcome == False


# a = BankAccount(1)
# print(a.test_insufficient_deposit())
# print(a.test_negative_deposit())
