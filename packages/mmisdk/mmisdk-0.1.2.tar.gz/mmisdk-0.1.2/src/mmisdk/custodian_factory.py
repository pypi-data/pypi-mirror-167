import requests

from mmisdk.common.custodian import Custodian
from mmisdk.qredo.qredo import Qredo

MMI_CONFIGURATION_API = "https://mmi-configuration-api.codefi.network/v1/configuration/default"


class CustodianFactory:
    """Use this utility class to instanciate custodians."""

    def __init__(self) -> None:
        try:
            response = requests.get(MMI_CONFIGURATION_API, timeout=1)
            custodians_config = response.json()["custodians"]
        except TimeoutError:
            print('The request timed out')
        else:
            self.custodians_config = custodians_config

    def create_for(self, custodian_name, refresh_token) -> Custodian:
        """"""
        configs_with_name = filter(
            lambda config: config["name"] == custodian_name, self.custodians_config)

        as_list = list(configs_with_name)

        assert len(
            as_list) > 0, f"Could not find a custodian with name {custodian_name}"
        assert len(
            as_list) < 2, f"Found multiple custodians with name {custodian_name}"

        result = as_list[0]

        # TODO Add more cases
        if custodian_name == 'qredo':
            # TODO Deal with this
            result["apiBaseUrl"] = "https://7ba211-api.qredo.net"
            return Qredo(result["name"], result["apiBaseUrl"], refresh_token)
        else:
            assert False, "Passed custodian client is not implemented"
