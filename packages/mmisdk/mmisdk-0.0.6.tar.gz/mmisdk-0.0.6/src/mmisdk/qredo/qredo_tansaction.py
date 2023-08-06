from typing import Dict
from typing import List
from typing import Optional

from pydantic import BaseModel


class QredoTransactionEvent(BaseModel):
    id: str
    timestamp: int
    status: str
    message: str


class QredoTransaction(BaseModel):
    txID: str
    txHash: str
    status: str
    timestamps: Dict
    events: List[QredoTransactionEvent]
    nonce: int
    gasLimit: str
    gasPrice: Optional[str]
    maxFeePerGas: Optional[str]
    maxPriorityFeePerGas: Optional[str]
    from_: str
    to: str
    value: str
    data: str
    rawTX: str
    createdBy: str
    accountID: str
    network: str
    chainID: str
