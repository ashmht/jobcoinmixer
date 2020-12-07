from http import HTTPStatus

from jobcoin.config import API_TRANSACTIONS_URL
from jobcoin.transactions import Transactions


class TestTransactions:
    def test_when_transfer_jobcoins_has_succeeded(self, requests_mock):
        source, destination, amount = "Alice", "Salah", "50"
        requests_mock.post(url=API_TRANSACTIONS_URL, status_code=HTTPStatus.OK)
        response = Transactions.transfer_jobcoins(
            source=source, destination=destination, amount=amount
        )
        assert response == f"{amount} JobCoins transferred to {destination}"

    def test_when_transfer_jobcoins_returns_insufficient_balance(self, requests_mock):
        source, destination, amount = "Alice", "Salah", "50"
        requests_mock.post(
            url=API_TRANSACTIONS_URL, status_code=HTTPStatus.UNPROCESSABLE_ENTITY
        )
        response = Transactions.transfer_jobcoins(
            source=source, destination=destination, amount=amount
        )
        assert response == f"Insufficient Balance"
