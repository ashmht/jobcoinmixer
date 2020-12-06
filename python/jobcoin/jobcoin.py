from decimal import Decimal
from typing import List, Dict
from uuid import UUID

from jobcoin.addresses import Addresses
from jobcoin.doler import Doler
from jobcoin.fee import Fee
from jobcoin.transactions import Transactions


class JobCoin:
    deposit_addresses: Dict[int, str]
    customer_address_map: Dict[int, List[str]]
    big_house_address: str

    def __init__(self, deposit_addresses, customer_address_map, big_house_address):
        self.deposit_addresses = deposit_addresses
        self.customer_address_map = customer_address_map
        self.big_house_address = big_house_address

    def provide_addresses(self, customer_id: int, unused_addresses: List[str]):
        self.customer_address_map[customer_id].extend(unused_addresses)

    def get_deposit_address(self, customer_id: int) -> str:
        deposit_address = str(UUID())
        self.deposit_addresses[customer_id] = deposit_address
        return deposit_address

    def detect_transfer(self, customer_id: int) -> bool:
        deposit_address = self.deposit_addresses.get(customer_id, False)
        if not deposit_address:
            return False
        # Get balance and transactions from deposit address
        balance, transactions = Addresses.get_balance_transactions(
            deposit_address=deposit_address
        )
        return bool(balance)

    def mix(self, customer_id: int, amount: str):
        if self.detect_transfer(customer_id=customer_id):
            Transactions.transfer_jobcoins(
                source=self.deposit_addresses[customer_id],
                destination=self.big_house_address,
                amount=amount,
            )
        self.dole(
            amount=Decimal(amount),
            customer_addresses=self.customer_address_map[customer_id],
        )

    def dole(self, amount: Decimal, customer_addresses: List[str]):
        disburse_amount: Decimal = Fee.detect_fee(amount, len(customer_addresses))
        print(disburse_amount)
        transaction_amounts: List[Decimal] = Doler.calculate_dole_amounts(
            amount, len(customer_addresses)
        )
        print(transaction_amounts)
        transaction_amounts: List[Decimal] = Doler.round_last(
            transactions=transaction_amounts
        )
        [
            Transactions.transfer_jobcoins(
                source=self.big_house_address,
                destination=destination,
                amount=transaction_amounts.pop(),
            )
            for destination in customer_addresses
        ]
