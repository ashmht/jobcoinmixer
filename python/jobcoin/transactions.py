from http import HTTPStatus

import requests

from jobcoin.config import API_TRANSACTIONS_URL


class Transactions:
    @staticmethod
    def transfer_jobcoins(source: str, destination: str, amount: str):
        transaction_details = dict(
            fromAddress=source, toAddress=destination, amount=amount
        )
        response = requests.post(url=API_TRANSACTIONS_URL, data=transaction_details,)
        if response.status_code == HTTPStatus.OK:
            print(f"{amount} JobCoins transferred from {source} to {destination}")
            return f"{amount} JobCoins transferred to {destination}"
        elif response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            print(f"Insufficient Balance from {source}")
            return "Insufficient Balance"
