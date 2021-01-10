import uuid

from jobcoin.addresses import Addresses
from jobcoin.config import API_ADDRESS_URL


class TestAddresses:
    def test_get_balance_transactions(self, requests_mock):
        deposit_address = uuid.uuid4().hex
        data = {"balance": "400", "transactions": []}
        requests_mock.get(url="/".join([API_ADDRESS_URL, deposit_address]), json=data)
        balance, transactions = Addresses.get_balance_transactions(
            deposit_address=deposit_address
        )
        assert balance, transactions == ("400", [])
