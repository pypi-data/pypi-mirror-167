from src.custodian_factory import CustodianFactory
from src.qredo.qredo import Qredo

# You can instanciate a custodian directly like so:
custodian0 = Qredo("qredo", "https://7ba211-api.qredo.net")
response0 = custodian0.get_transaction("1yiq2w7NSFei1uyQOremLiwbP2I")
print(response0.json())

# However it's simpler to rely on the factory
# It figures out itself which api URL to use
factory = CustodianFactory()
custodian1 = factory.create_for("qredo")
response1 = custodian1.get_transaction("1yiq2w7NSFei1uyQOremLiwbP2I")
print(response1.json())

# {
# 	"txID": "1yak0mq127EZ8Ru2RjpErdqmQHs",
# 	"txHash": "0x83ea89a36861244a2b41768ac19d3c35d94f11beae200c5feaaa0e913188b606",
# 	"status": "confirmed",
# 	"timestamps": {
# 		"approved": 1632496883,
# 		"authorized": 1632496865,
# 		"confirmed": 1632496936,
# 		"created": 1632496865,
# 		"pushed": 1632496887,
# 		"queued": 1632496883,
# 		"signed": 1632496885
# 	},
# 	"events": [
# 		{
# 			"id": "1yak0lSnaNBt7CKFrsqXbUopUH2",
# 			"timestamp": 1632496865,
# 			"status": "authorized",
# 			"message": ""
# 		},
#    ...
# 	],
# 	"nonce": 2,
# 	"gasPrice": "1100000011",
# 	"gasLimit": "34062",
# 	"from": "0x6cF8426Cf36B1f43ffF6C376d290114297441bc2",
# 	"to": "0x722dd3F80BAC40c951b51BdD28Dd19d435762180",
# 	"value": "0",
# 	"data": "0x97c5ed1e0000000000000000000000007e654d251da770a068413677967f6d3ea2fea9e40000000000000000000000000000000000000000000000000de0b6b3a7640000",
# 	"rawTX": "-GgChEGQqwuChQ6Uci3T-AusQMlRtRvdKN0Z1DV2IYCAuESXxe0eAAAAAAAAAAAAAAAAfmVNJR2ncKBoQTZ3ln9tPqL-qeQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN4Lazp2QAAICAgA",
# 	"createdBy": "39XVDZMAxWjZNBqSHqt2MbHzjkBDqUDmGCdmcN3icDs5",
# 	"accountID": "1yXIvPBU5rgZJhccR9LFQlYMqLN",
# 	"network": "",
# 	"chainID": ""
# }
