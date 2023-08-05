""" User Stores Get Controller Definition """

from rowantree.contracts import UserStores

from .abstract_controller import AbstractController


class UserStoresGetController(AbstractController):
    """
    User Stores Get Controller
    Gets the (unique) list of user stores.

    Methods
    -------
    execute(self, user_guid: str) -> UserStores
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserStores:
        """
        Gets the (unique) list of user stores.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_stores: UserStores
            A (unique) list of user stores.
        """

        return self.dao.user_stores_get(user_guid=user_guid)
