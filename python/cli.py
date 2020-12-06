#!/usr/bin/env python
import uuid
import sys
from collections import defaultdict
from random import randrange
from typing import Dict, List

import click

from jobcoin import jobcoin
from jobcoin.jobcoin import JobCoin
from jobcoin.transactions import Transactions


@click.command()
def main(args=None):
    print("Welcome to the Jobcoin mixer!\n")
    deposit_addresses: Dict[int, List[str]] = defaultdict(list)
    while True:
        addresses = click.prompt(
            "Please enter a comma-separated list of new, unused Jobcoin "
            "addresses where your mixed Jobcoins will be sent.",
            prompt_suffix="\n[blank to quit] > ",
            default="",
            show_default=False,
        )
        if addresses.strip() == "":
            sys.exit(0)
        customer_id = randrange(2000)
        big_house_address = uuid.uuid4().hex
        jobcoin = JobCoin(
            deposit_addresses={},
            customer_address_map=defaultdict(list),
            big_house_address=big_house_address,
        )
        deposit_address = jobcoin.get_deposit_address(customer_id=customer_id)
        jobcoin.provide_addresses(
            customer_id=customer_id, unused_addresses=addresses.split(",")
        )
        click.echo(
            "\nYou may now send Jobcoins to address {deposit_address}. They "
            "will be mixed and sent to your destination addresses.\n".format(
                deposit_address=deposit_address
            )
        )
        amount_to_mix = "100"
        Transactions.transfer_jobcoins(
            source="Alice", destination=deposit_address, amount=amount_to_mix
        )
        jobcoin.mix(customer_id=customer_id, amount=amount_to_mix)


if __name__ == "__main__":
    sys.exit(main())
