from algosdk import account
from algosdk.atomic_transaction_composer import AccountTransactionSigner, AtomicTransactionComposer

from algorand_governance_oracle.application import contract


example_values = {
    "period_identifier": "governance-period-4".encode(),

    "eligible_committed_stake": 3788144125919121,
    "ineligible_committed_stake": 295846447001842,

    "eligible_governor_count": 32677,
    "ineligible_governor_count": 1923,

    "algo_amount_in_reward_pool": 70500000000000,

    "updated_at": 1662985556,
}


def construct_method_arguments(values):
    method_args = list()
    method_args.append(values.pop("period_identifier"))

    method_args.append(values.pop("eligible_committed_stake"))
    method_args.append(values.pop("ineligible_committed_stake"))

    method_args.append(values.pop("eligible_governor_count"))
    method_args.append(values.pop("ineligible_governor_count"))

    method_args.append(values.pop("algo_amount_in_reward_pool"))

    method_args.append(values.pop("updated_at"))

    if values:
        raise ValueError(f"There are unsupported method arguments: {values}")

    return method_args


def update(algod_client, private_key, application_id, values):
    sender = account.address_from_private_key(private_key)
    signer = AccountTransactionSigner(private_key)

    sp = algod_client.suggested_params()

    atc = AtomicTransactionComposer()

    method_args = construct_method_arguments(values)
    atc.add_method_call(
        app_id=application_id,
        method=contract.get_method_by_name("update"),
        sender=sender,
        sp=sp,
        signer=signer,
        method_args=method_args,
    )

    results = atc.execute(algod_client, 5)
    transaction_id = results.tx_ids[0]

    return transaction_id
