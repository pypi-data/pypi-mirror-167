""" User Features Active Get Controller Definition """

from rowantree.contracts import UserFeature

from .abstract_controller import AbstractController


class UserFeaturesActiveGetController(AbstractController):
    """
    User Features Active Get Controller
    Gets the active user feature.

    Methods
    -------
    execute(self, user_guid: str, details: bool) -> UserFeature
        Executes the command.
    """

    def execute(self, user_guid: str, details: bool) -> UserFeature:
        """
        Gets the active user feature.

        Parameters
        ----------
        user_guid: str
            The target user guid.
        details: bool
            Whether to include details of the feature.

        Returns
        -------
        user_feature: UserFeature
            The active UserFeature.
        """

        if details:
            feature: UserFeature = self.dao.user_active_feature_state_details_get(user_guid=user_guid)
        else:
            feature: UserFeature = self.dao.user_active_feature_get(user_guid=user_guid)
        return feature
