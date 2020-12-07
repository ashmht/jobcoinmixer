from decimal import Decimal


class Fee(object):
    TWO_PLACES = Decimal(10) ** -2

    @staticmethod
    def calculate_charge(amount: Decimal, num_transactions: int) -> Decimal:
        fees = Fee.calculate_fee(amount=amount, num_transactions=num_transactions)
        charge = (amount - fees).quantize(Fee.TWO_PLACES)
        print(f"Fees is {(amount - charge).quantize(Fee.TWO_PLACES)}")
        print(f"Charge is {charge}")
        return charge

    @staticmethod
    def calculate_fee(amount: Decimal, num_transactions: int) -> Decimal:
        # 2.5% + (2.5) ^ (num of transactions)
        return (
            amount * (Decimal(0.025) + Decimal(0.025) ** num_transactions)
        ).quantize(Fee.TWO_PLACES)
