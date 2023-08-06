from abc import abstractmethod

from mmisdk.common.transaction import Transaction


class Custodian:
    """Generic class that each custodian client must inherit from."""

    def __init__(self, name, api_url, refresh_token):
        self.name = name
        self.api_url = api_url
        self.refresh_token = refresh_token

    @abstractmethod
    def get_transaction(self, transaction_id) -> Transaction:
        """Query the custodian's API to fetch details about the transaction of passed id."""
        pass

    @abstractmethod
    def create_transaction(self, tx_params) -> Transaction:
        """Create a transaction from the passed parameters a send it to the custodian's API."""
        pass
