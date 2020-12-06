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
            return f"{amount} JoinCoins transferred to {destination}"
        elif response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
            return "Insufficient Balance"
