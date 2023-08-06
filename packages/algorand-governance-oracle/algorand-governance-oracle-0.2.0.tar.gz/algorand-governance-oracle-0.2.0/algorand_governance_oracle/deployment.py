import base64

from algosdk.account import address_from_private_key
from algosdk.future.transaction import OnComplete, ApplicationCreateTxn, wait_for_confirmation, StateSchema

from algorand_governance_oracle.application import approval_program, clear_program


def compile_program(algod_client, source_code):
    compile_response = algod_client.compile(source_code)
    return base64.b64decode(compile_response['result'])


def create_application(algod_client, private_key, approval_program_compiled, clear_program_compiled, global_schema, local_schema):
    # define sender as creator
    sender = address_from_private_key(private_key=private_key)

    # declare on_complete as NoOp
    on_complete = OnComplete.NoOpOC.real

    # get node suggested parameters
    params = algod_client.suggested_params()

    # create unsigned transaction
    txn = ApplicationCreateTxn(
        sender=sender,
        sp=params,
        on_complete=on_complete,
        approval_program=approval_program_compiled,
        clear_program=clear_program_compiled,
        global_schema=global_schema,
        local_schema=local_schema
    )

    # sign transaction
    signed_transaction = txn.sign(private_key=private_key)
    transaction_id = signed_transaction.transaction.get_txid()

    # send transaction
    algod_client.send_transactions([signed_transaction])

    # wait for confirmation
    transaction_response = wait_for_confirmation(
        algod_client=algod_client,
        txid=transaction_id,
        wait_rounds=4
    )
    print("TXID: ", transaction_id)
    print("Result confirmed in round: {}".format(transaction_response['confirmed-round']))

    # display results
    transaction_response = algod_client.pending_transaction_info(transaction_id=transaction_id)
    app_id = transaction_response['application-index']
    print("Created new app-id:", app_id)

    return app_id


def create_oracle_application(algod_client, private_key):
    local_ints = 0
    local_bytes = 0
    global_ints = 32
    global_bytes = 32

    global_schema = StateSchema(num_uints=global_ints, num_byte_slices=global_bytes)
    local_schema = StateSchema(num_uints=local_ints, num_byte_slices=local_bytes)

    approval_program_compiled = compile_program(algod_client=algod_client, source_code=approval_program)
    clear_program_compiled = compile_program(algod_client=algod_client, source_code=clear_program)

    application_id = create_application(
        algod_client=algod_client,
        private_key=private_key,
        approval_program_compiled=approval_program_compiled,
        clear_program_compiled=clear_program_compiled,
        global_schema=global_schema,
        local_schema=local_schema,
    )

    return application_id
