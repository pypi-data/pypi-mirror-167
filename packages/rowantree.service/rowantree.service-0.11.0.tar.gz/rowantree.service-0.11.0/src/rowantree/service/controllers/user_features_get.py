""" User Features Get Controller Definition """

from rowantree.contracts import UserFeatures

from .abstract_controller import AbstractController


class UserFeaturesGetController(AbstractController):
    """
    User Features Get Controller
    Gets the unique list of user features.

    Methods
    -------
    execute(self, user_guid: str) -> UserFeatures
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserFeatures:
        """
        Gets the unique list of user features.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_features: UserFeatures
            A unique list of user features.
        """

        return self.dao.user_features_get(user_guid=user_guid)
