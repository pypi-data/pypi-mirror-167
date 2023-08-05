""" User Delete Controller Definition """

from typing import Any

from .abstract_controller import AbstractController


class UserDeleteController(AbstractController):
    """
    User Delete Controller
    Deletes a user.

    Methods
    -------
    execute(self, user_guid: str) -> None
        Executes the command.
    """

    def execute(self, user_guid: str) -> Any:
        """
        Deletes a user.

        Parameters
        ----------
        user_guid: str
            The target user guid.
        """

        return self.dao.user_delete(user_guid=user_guid)
