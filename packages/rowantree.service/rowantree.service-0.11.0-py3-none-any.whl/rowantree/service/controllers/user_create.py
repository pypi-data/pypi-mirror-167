""" User Create Controller Definition """

from rowantree.contracts import User

from .abstract_controller import AbstractController


class UserCreateController(AbstractController):
    """
    User Create Controller
    Creates a user.

    Methods
    -------
    execute(self) -> User
        Executes the command.
    """

    def execute(self, request: str) -> User:
        """
        Creates a user.

        Returns
        -------
        user: User
            The newly created user.
        """

        return self.dao.user_create_by_guid(user_guid=request)
