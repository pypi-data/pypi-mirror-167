""" User Transport Controller Definition """

from rowantree.contracts import UserFeature
from rowantree.service.sdk import UserTransportRequest

from .abstract_controller import AbstractController


class UserTransportController(AbstractController):
    """
    User Transport Controller
    Performs a user transport. (feature to feature change)

    Methods
    -------
    execute(self, user_guid: str, request: UserTransportRequest) -> UserFeature
        Executes the command.
    """

    def execute(self, user_guid: str, request: UserTransportRequest) -> UserFeature:
        """
        Performs a user transport. (feature to feature change)

        Parameters
        ----------
        user_guid: str
            The target user guid.
        request: UserTransportRequest
            The UserTransportRequest to perform.

        Returns
        -------
        user_feature: UserFeature
            The user's new active feature.
        """

        return self.dao.user_transport(user_guid=user_guid, location=request.location)
