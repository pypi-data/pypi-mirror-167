from mmisdk import CustodianFactory
from mmisdk import Qredo

# You can instanciate a custodian directly like so:
custodian0 = Qredo("qredo", "https://7ba211-api.qredo.net", "YOUR-REFRESH-TOKEN")
response0 = custodian0.get_transaction("1yiq2w7NSFei1uyQOremLiwbP2I")
print(response0.json())

# However it's simpler to rely on the factory
# It figures out itself which api URL to use
factory = CustodianFactory()
custodian1 = factory.create_for("qredo", "2ECrQyuycg6l4kjRGcnXvHzr87y-20984763496da41fc582ad946742f019")
response1 = custodian1.get_transaction("1yiq2w7NSFei1uyQOremLiwbP2I")
print(response1.json())

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
