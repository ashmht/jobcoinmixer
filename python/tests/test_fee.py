from decimal import Decimal

from jobcoin.fee import Fee


class TestFee:
    def test_calculate_fee(self):
        assert Decimal("10.00") == Fee.calculate_fee(
            amount=Decimal("200"), num_transactions=1
        )

    def test_calculate_fee_with_more_transactions(self):
        assert Decimal("0.50") == Fee.calculate_fee(
            amount=Decimal("20"), num_transactions=10
        )

    def test_calculate_charge(self):
        assert Decimal("156.48") == Fee.calculate_charge(
            amount=Decimal("160.50"), num_transactions=3
        )

    def test_calculate_charge_with_more_transactions(self):
        assert Decimal("5850.00") == Fee.calculate_charge(
            amount=Decimal("6000"), num_transactions=5
        )
