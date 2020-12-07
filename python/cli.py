#!/usr/bin/env python
import sys
from collections import defaultdict
from random import randrange

import click

from jobcoin.jobcoin import JobCoin
from jobcoin.mixer import Mixer
from jobcoin.transactions import Transactions


@click.command()
def main(args=None):
    print("Welcome to the Jobcoin mixer!\n")
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
        jobcoin = JobCoin(
            deposit_addresses={},
            customer_address_map=defaultdict(list),
            big_house_address="BigHouse",
        )
        deposit_address = jobcoin.get_deposit_address(customer_id=customer_id)
        addresses = list(filter(None, addresses.split(",")))
        jobcoin.provide_addresses(customer_id=customer_id, unused_addresses=addresses)
        click.echo(
            "\nYou may now send Jobcoins to address {deposit_address}. They "
            "will be mixed and sent to your destination addresses.\n".format(
                deposit_address=deposit_address
            )
        )
        amount_to_mix = "20"
        Transactions.transfer_jobcoins(
            source="Alice", destination=deposit_address, amount=amount_to_mix
        )
        mixer = Mixer(jobcoin=jobcoin)
        mixer.mix(
            big_house_address="BigHouse", customer_id=customer_id, amount=amount_to_mix,
        )


if __name__ == "__main__":
    sys.exit(main())
