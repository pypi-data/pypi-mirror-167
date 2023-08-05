from typing import Optional

from pydantic import BaseModel


class QredoTxDetails(BaseModel):
    chainId: str
    note: Optional[str]
