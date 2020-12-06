from decimal import Decimal
from typing import List

from numpy.random import multinomial


class Doler:
    @classmethod
    def calculate_dole_amounts(cls, amount: Decimal, num_transactions: int):
        return cls.round_last(
            [
                Decimal(i.item())
                for i in multinomial(
                    int(amount), [1 / num_transactions] * num_transactions
                )
            ]
        )

    @classmethod
    def round_last(cls, transactions: List[Decimal]):
        last_transaction = transactions.pop()
        rounded_amount = last_transaction % 1
        transactions.append(last_transaction + rounded_amount)
        return transactions
