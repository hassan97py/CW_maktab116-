import pytest
from q import BankAccount
class TestBankAccount:
    def setup_method(self):
        self.account1 = BankAccount(100)  # Initial balance of 100
        self.account2 = BankAccount(50)    # Initial balance of 50

    def test_deposit(self):
        self.account1.deposit(50)
        assert self.account1.get_balance() == 150

    def test_withdraw(self):
        self.account1.withdraw(30)
        assert self.account1.get_balance() == 70

    def test_withdraw_insufficient_funds(self):
        with pytest.raises(ValueError, match="Insufficient funds."):
            self.account1.withdraw(200)

    def test_get_balance(self):
        assert self.account1.get_balance() == 100

    def test_transfer(self):
        self.account1.transfer(50, self.account2)
        assert self.account1.get_balance() == 50
        assert self.account2.get_balance() == 100

    def test_transfer_insufficient_funds(self):
        with pytest.raises(ValueError, match="Insufficient funds."):
            self.account1.transfer(200, self.account2)

    def test_transfer_negative_amount(self):
        with pytest.raises(ValueError, match="Transfer amount must be positive."):
            self.account1.transfer(-50, self.account2)

    def test_deposit_negative_amount(self):
        with pytest.raises(ValueError, match="Deposit amount must be positive."):
            self.account1.deposit(-20)

    def test_withdraw_negative_amount(self):
        with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
            self.account1.withdraw(-20)

if __name__ == "__main__":
    pytest.main()
