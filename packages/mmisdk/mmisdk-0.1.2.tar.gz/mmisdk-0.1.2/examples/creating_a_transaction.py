from mmisdk import CustodianFactory

# Instantiate the factory
factory = CustodianFactory()

# Create the custodian, using the factory
custodian = factory.create_for("qredo", "YOUR-REFRESH-TOKEN")

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
#   "id": "1yiq2w7NSFei1uyQOremLiwbP2I",
#   "type": "1",
#   "from_": "0x6cF8426Cf36B1f43ffF6C376d290114297441bc2",
#   "to": "0x722dd3F80BAC40c951b51BdD28Dd19d435762180",
#   "value": "0",
#   "gas": "34062",
#   "gasPrice": "1000000010",
#   "maxPriorityFeePerGas": null,
#   "maxFeePerGas": null,
#   "nonce": "3",
#   "data": "0x97c5ed1e....",
#   "hash": "0xf31f4aa0d29e9d52a0f6de6dbb191f6060fd8bc994cea5c8785b2a94301a140c",
#   "status": {
#     "finished": false,
#     "submitted": true,
#     "signed": true,
#     "success": false,
#     "displayText": "Confirmed",
#     "reason": "Unknown"
#   }
# }
