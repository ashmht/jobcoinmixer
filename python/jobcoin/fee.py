from decimal import Decimal


class Fee(object):
    TWO_PLACES = Decimal(10) ** -2

    @classmethod
    def detect_fee(cls, amount: Decimal, num_transactions: int) -> Decimal:
        fees = cls.calculate_fee(amount=amount, num_transactions=num_transactions)
        charge = amount - fees
        return charge.quantize(cls.TWO_PLACES)

    @classmethod
    def calculate_fee(cls, amount: Decimal, num_transactions: int) -> Decimal:
        # 2.5% + (2.5) ^ (num of transactions)
        return amount * (Decimal(0.025) + Decimal(0.025) ** num_transactions)
