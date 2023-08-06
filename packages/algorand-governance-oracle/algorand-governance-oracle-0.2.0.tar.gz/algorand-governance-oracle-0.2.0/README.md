# Algorand Governance Oracle

It is an "oracle" for Algorand Governance.

- Mainnet Application ID: `will go here`
- Testnet Application ID: [`109903471`](https://testnet.algoexplorer.io/application/109903471)

## Application State

We'll have how to use application state in other application.

## Development and Update

### How to create new application

```python
from algorand_governance_oracle.deployment import create_oracle_application
from algorand_governance_oracle.clients import testnet_algod_client

private_key = "put your private key in here."

application_id = create_oracle_application(algod_client=testnet_algod_client, private_key=private_key)

print(application_id)
```

### How to update application state with statistics

```python
from algorand_governance_oracle.api import update
from algorand_governance_oracle.clients import testnet_algod_client

private_key = "put your private key in here."
application_id = "put your application id in here."

values = {
    "period_identifier": "governance-period-4".encode(),

    "eligible_committed_stake": 3788144125919121,
    "ineligible_committed_stake": 295846447001842,

    "eligible_governor_count": 32677,
    "ineligible_governor_count": 1923,

    "algo_amount_in_reward_pool": 70500000000000,

    "updated_at": 1662985556,
}

transaction_id = update(
    algod_client=testnet_algod_client,
    private_key=private_key, 
    application_id=application_id,
    values=values,
)

print(transaction_id)
```
