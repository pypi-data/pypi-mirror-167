# MMI Custodian SDK

A Python library to create and submit EVM transactions to custodians connected with MetaMask Institutional.

## Installing

```sh
pip3 install mmisdk
```

## Getting started

```python
from mmisdk import CustodianFactory

factory = CustodianFactory()

# Instiate a Qredo client with a refresh token
custodian = factory.create_for(
    "qredo", "YOUR-REFRESH-TOKEN")
```

## Creating a transaction

```python
tx_params = {
  "data" : "0x031E223FabC1Da031E223FabC1Da031E223FabC1Da031E223FabC1Da031E223FabC1Da",
  "from": "0xb2c77973279baaaf48c295145802695631d50c01",
  "to": "0x57f36031E223FabC1DaF93B401eD9F4F1Acc6904",
  "type": "0x2",
  "value": "0x1",
  "gas": "0x5208",
  "maxFeePerGas": "0x59682f0e",
  "maxPriorityFeePerGas": "0x59682f0e"
}

qredo_tx_details = {
  "chainId": "0x4",
  "originUrl": "https://www.example.com"
}

transaction = custodian.create_transaction(qredo_tx_details, tx_params)

# Getting the status of a transaction you have created
custodian.get_transaction(transaction.id)

print(result)

# {
#   "id": "ef8cb7af-1a00-4687-9f82-1f1c82fbef54",
#   "type": "0x2",
#   "from": "0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826",
#   "to": "0xB8c77482e45F1F44dE1745F52C74426C631bDD52",
#   "value": "0x0",
#   "gas": "0x5208",
#   "gasPrice": "0x4A817C800",
#   "nonce": "0x1",
#   "data": "0x",
#   "hash": "0x1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
#   "status": {
#     "finished": true,
#     "submitted": true,
#     "signed": true,
#     "success": true,
#     "displayText": "Mined"
#   }
# }
```

You can see a list of supported custodians and API URLs here
https://mmi-configuration-api.codefi.network/v1/configuration/default. Use the custodian's field `name` in the code below to instanciate a client for the right custodian.

| Custodian  | Supported | As of version | Factory name param |
| ---------- | --------- | ------------- | ------------------ |
| Qredo      | ✅        | 0.0.0         | `"qredo"`          |
| All others | ❌        |               |                    |

## Subscribing to transaction events

🚨 NOT IMPLEMENTED YET

```python
def log_event(event, *args, **kwargs):
    log.debug('%s %s %s', event, args, kwargs)

custodian.on('transaction-update', log_event)
```

## MVP Scope

-   Works with one custodian type (either Qredo or JSON-RPC)
-   Library published on pypi for python3 only

## Developer documentation

For instructions about development, testing, building and release, check the [developer documentation](https://gitlab.com/ConsenSys/codefi/products/mmi/mmi-sdk-py).
