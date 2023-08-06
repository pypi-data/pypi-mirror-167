from algosdk.v2client.algod import AlgodClient


testnet_algod_client = AlgodClient(
    algod_address="https://testnet-api.algonode.cloud",
    algod_token="",
    headers={
        "User-Agent": "algosdk",
    }
)
