Assumptions

The currency of the amount is same.
The API are available 100%
No error handling needed.
We are assuming "Alice" as the user with amount=20.

Design Decisions

Using separation of concerns, we have

Transactions - Calls Transactions API to transfer jobcoins

Addresses - Calls Addresses API to check balance on an address

Fee - Calculates Fees and Charge

Doler - Calculate dole amounts and creates transactions

Mixer - Entry point to mix coins. 

Tradeoffs

The mixer only have 1 level of redirection to obfuscate the transaction trail. Ideally, I would like to have 3.
The BigHouse Address would be a pool of addresses rather than a single one used here.

Also we could maintain an internal mapping of customers and their hashed addresses instead plain_text address, if 
in case the transactions are compromised.

We could also hash the amounts if someone tried to use combinatorial brute force.
These are potential TODOs in addition to writing more tests. 