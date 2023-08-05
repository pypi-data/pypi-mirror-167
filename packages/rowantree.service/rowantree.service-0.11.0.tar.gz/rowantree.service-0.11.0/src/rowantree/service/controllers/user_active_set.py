""" User Active Set Controller Definition """

from rowantree.contracts import UserActive

from ..services.db.dao import DBDAO
from .abstract_controller import AbstractController


class UserActiveSetController(AbstractController):
    """
    User Active Set Controller
    Sets the user active state.

    Methods
    -------
    execute(self, user_guid: str, request: UserActive) -> UserActive
        Executes the command.
    """

    def __init__(self, dao: DBDAO):
        super().__init__(dao=dao)

    def execute(self, user_guid: str, request: UserActive) -> UserActive:
        """
        Sets the user active state.

        Parameters
        ----------
        user_guid: str
            The user guid to target.
        request: UserActive
            The active state to set the user to.

        Returns
        -------
        user_active: UserActive
            The state of the user.
        """

        self.dao.user_active_state_set(user_guid=user_guid, active=request.active)
        return request
