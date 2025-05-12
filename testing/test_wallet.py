import pytest
from wallet import Wallet, InsufficientAmount

"""
# refactoring using fixtures 
We define two fixture functions - wallet and empty_wallet, 
which will be responsible for initializing the Wallet class in tests where it is needed, with different values.
"""

import pytest
from wallet import Wallet, InsufficientAmount


@pytest.fixture
def empty_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest.fixture
def wallet():
    """Returns a Wallet instance with a balance of 20"""
    return Wallet(20)


def test_default_initial_amount(empty_wallet):
    print("\nRunning test_default_initial_amount...")
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    print("\nRunning test_setting_initial_amount...")
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    print("\nRunning test_wallet_add_cash...")
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    print("\nRunning test_wallet_spend_cash...")
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(
    empty_wallet,
):
    print(
        "\nRunning test_wallet_spend_cash_raises_exception_on_insufficient_amount..."
    )
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


@pytest.fixture
def my_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest.mark.parametrize(
    "earned,spent,expected",
    [
        (30, 10, 20),
        (20, 2, 18),
    ],
)
def test_transactions(earned, spent, expected, my_wallet):
    print(
        f"\nRunning test_transactions with earned={earned}, spent={spent}, expected={expected}..."
    )
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected


"""
def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(10)
    wallet.add_cash(90)
    assert wallet.balance == 100

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount():
    wallet = Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)

"""
