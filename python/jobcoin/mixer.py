from decimal import Decimal
from typing import Tuple

from jobcoin.addresses import Addresses
from jobcoin.doler import Doler
from jobcoin.jobcoin import JobCoin
from jobcoin.transactions import Transactions


class Mixer:
    def __init__(self, jobcoin: JobCoin):
        self.jobcoin = jobcoin

    @staticmethod
    def detect_transfer(deposit_address: str) -> Tuple[bool, str]:
        # Get balance and transactions from deposit address
        balance, transactions = Addresses.get_balance_transactions(
            deposit_address=deposit_address
        )
        print(f"Deposit address has balance: {balance}")
        return bool(Decimal(balance)), balance

    def mix(self, big_house_address: str, customer_id: int):
        deposit_address = self.jobcoin.get_deposit_address(customer_id=customer_id)
        customer_addresses = self.jobcoin.get_customer_addresses(
            customer_id=customer_id
        )
        has_balance, amount = self.detect_transfer(deposit_address=deposit_address)
        if has_balance:
            Transactions.transfer_jobcoins(
                source=deposit_address, destination=big_house_address, amount=amount,
            )
            Doler.dole(
                big_house_address=big_house_address,
                amount=Decimal(amount),
                customer_addresses=customer_addresses,
            )
