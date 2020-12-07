import time
from datetime import datetime
from decimal import Decimal
from itertools import cycle
from random import randrange
from typing import List

from numpy.random import multinomial

from jobcoin.fee import Fee
from jobcoin.transactions import Transactions


class Doler:
    @classmethod
    def calculate_dole_amounts(cls, amount: Decimal, num_transactions: int):
        return cls.round_last(
            transactions=[
                Decimal(i.item())
                # Split amount into num_transactions where range(1, amount) has equal probability
                for i in multinomial(
                    int(amount), [1 / num_transactions] * num_transactions
                )
            ],
            disburse_amount=amount,
        )

    @classmethod
    def round_last(cls, transactions: List[Decimal], disburse_amount: Decimal):
        # Add the fractional value to the last transaction_amount
        # If disburse_amount is 10.5 and transactions are 3,2,4, 1, this changes 1 to 1.5
        rounded_amount = disburse_amount % 1
        transactions[-1] += rounded_amount
        return transactions

    @classmethod
    def dole(cls, big_house_address, amount: Decimal, customer_addresses: List[str], delay: bool = True):
        disburse_amount: Decimal = Fee.calculate_charge(amount, len(customer_addresses))
        # Have at least 3 transactions
        num_transactions = max(3, len(customer_addresses))
        transaction_amounts: List[Decimal] = Doler.calculate_dole_amounts(
            amount=disburse_amount, num_transactions=num_transactions
        )
        transaction_amounts = list(filter(lambda num: num != 0, transaction_amounts))
        transaction_log: List[str] = []
        for destination, amount in zip(cycle(customer_addresses), transaction_amounts):
            # Wait randomly for (1,10) seconds
            if delay:
                time.sleep(randrange(10))
            print(f"Sending {amount} to {destination} at {datetime.now()}")
            transaction_log.append(f"Sending {amount} to {destination}")
            Transactions.transfer_jobcoins(
                source=big_house_address, destination=destination, amount=str(amount),
            )
        return transaction_log

