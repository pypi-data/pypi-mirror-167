"""Bite"""

from pydantic import BaseModel
from typing import Optional


class QredoTxDetails(BaseModel):
    chainId: str
    note: Optional[str]
