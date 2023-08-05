from src.custodian_factory import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Create the custodian, using the factory
custodian = factory.create_for("qredo")

# Build the transaction payload
txParams = {
    "from": "0x62468FD916bF27A3b76d3de2e5280e53078e13E1",
    "value": "1",
    "gasPrice": "25000000",
    "gasLimit": "21000",
    "data": ""
}
metadata = {
    "chainId": "0x4",
    "originUrl": "https://www.example.com"
}

# Send the transaction to the custodian
transaction_id = custodian.create_transaction(
    txParams, metadata)

# Getting the status of a transaction you have created
result = custodian.get_transaction(transaction_id)

print(result)

# {
#     "txID": "2ECtRwnaBca8kfeCh0dexFo21cq",
#     "txHash": "",
#     "status": "created",
#     "timestamps": {
#             "created": 1662111389
#     },
#     "events": [
#         {
#             "id": "2ECtRygA1kldo0MUVogx1zObIix",
#             "timestamp": 1662111389,
#             "status": "created",
#             "message": ""
#         }
#     ],
#     "nonce": 0,
#     "gasPrice": "25000000",
#     "gasLimit": "21000",
#     "from": "0x62468FD916bF27A3b76d3de2e5280e53078e13E1",
#     "to": "",
#     "value": "1",
#     "data": "",
#     "rawTX": "z4CEAX14QIJSCIABgICAgA",
#     "createdBy": "EFvSMt9uGTEsDCx22sYB8BPz1bCyxAZNPKDWpJVsLKM9",
#     "accountID": "2ECrNK9dUlYIpdI4xVuRQ4Diuwq",
#     "network": "",
#     "chainID": "3"
# }
