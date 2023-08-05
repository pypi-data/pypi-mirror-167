from src.custodian_factory import CustodianFactory

factory = CustodianFactory()

# Instiate a Qredo client with a refresh token
custodian = factory.create_for(
    "qredo", "YOUR-REFRESH-TOKEN")

# Build tx details
qredo_tx_details = {
    "chainId": 1,
    "note": "test"
}
tx_params = {
    "from_": "0x62468FD916bF27A3b76d3de2e5280e53078e13E1",
    "to": "0x62468FD916bF27A3b76d3de2e5280e53078e13E1",
    "value": "1",
    "gasLimit": "21000",
    "gasPrice": "1000",
    "data": "",
    # "type": "2"
    # "maxPriorityFeePerGas": "12321321",
    # "maxFeePerGas": "12321321",
}

# Create the tx from details and send it to the custodian
transaction = custodian.create_transaction(qredo_tx_details, tx_params)
print(transaction)

# Get the created transaction
result = custodian.get_transaction(transaction.id)
print(result)

# {
#   "txID": "2ECwd0i2NxqGeup4rv7sUcAbXXt",
#   "txHash": "",
#   "status": "created",
#   "timestamps": { "created": 1662112957 },
#   "events": [
#     {
#       "id": "2ECwcz3jQxkcTFuDEar03xmXQC6",
#       "timestamp": 1662112957,
#       "status": "created",
#       "message": ""
#     }
#   ],
#   "nonce": 0,
#   "gasPrice": "25000000",
#   "gasLimit": "21000",
#   "from": "0x62468FD916bF27A3b76d3de2e5280e53078e13E1",
#   "to": "",
#   "value": "1",
#   "data": "",
#   "rawTX": "z4CEAX14QIJSCIABgICAgA",
#   "createdBy": "EFvSMt9uGTEsDCx22sYB8BPz1bCyxAZNPKDWpJVsLKM9",
#   "accountID": "2ECrNK9dUlYIpdI4xVuRQ4Diuwq",
#   "network": "",
#   "chainID": "3"
# }
