from decimal import Decimal

import pytest

from jobcoin.doler import Doler


@pytest.fixture
def transactions():
    return [Decimal(i) for i in [3, 2, 1, 4]]


class TestDoler:
    def test_round_last_when_disburse_amount_has_fractional_value(self, transactions):
        assert Doler.round_last(
            transactions=transactions, disburse_amount=Decimal("10.75")
        ) == [Decimal(i) for i in [3, 2, 1, 4.75]]

    def test_round_last_when_disburse_amount_has_no_fractional_value(
        self, transactions
    ):
        assert Doler.round_last(
            transactions=transactions, disburse_amount=Decimal("10")
        ) == [Decimal(i) for i in [3, 2, 1, 4]]
