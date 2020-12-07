import uuid
from typing import List, Dict


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
        if self.deposit_addresses.get(customer_id, False):
            return self.deposit_addresses.get(customer_id)
        deposit_address = str(uuid.uuid4().hex)
        self.deposit_addresses[customer_id] = deposit_address
        return deposit_address

    def get_customer_addresses(self, customer_id: int) -> List[str]:
        return self.customer_address_map.get(customer_id, [])
