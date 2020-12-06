from http import HTTPStatus
from typing import List, Dict

import requests

from jobcoin.config import API_ADDRESS_URL


class Addresses:
    @staticmethod
    def get_balance_transactions(deposit_address: str):
        response = requests.get(url="/".join([API_ADDRESS_URL, deposit_address]))
        if response.status_code == HTTPStatus.OK:
            data = response.json()
            balance: str = data.get("balance")
            transactions: List[Dict[str, str]] = data.get("transactions")
            return balance, transactions
