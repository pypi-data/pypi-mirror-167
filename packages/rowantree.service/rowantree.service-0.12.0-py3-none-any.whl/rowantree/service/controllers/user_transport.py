""" User Transport Controller Definition """
import logging

from starlette import status
from starlette.exceptions import HTTPException

from rowantree.contracts import FeatureType
from rowantree.service.sdk import ActiveFeatureResponse, UserTransportRequest

from ..services.db.incorrect_row_count_error import IncorrectRowCountError
from .abstract_controller import AbstractController


class UserTransportController(AbstractController):
    """
    User Transport Controller
    Performs a user transport. (feature to feature change)

    Methods
    -------
    execute(self, user_guid: str, request: UserTransportRequest) -> ActiveFeatureResponse
        Executes the command.
    """

    def execute(self, user_guid: str, request: UserTransportRequest) -> ActiveFeatureResponse:
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
        user_feature: ActiveFeatureResponse
            The user's new active feature.
        """

        try:
            feature: FeatureType = self.dao.user_transport(user_guid=user_guid, location=request.location)
            return ActiveFeatureResponse(active_feature=feature)
        except IncorrectRowCountError as error:
            logging.debug("caught: {%s}", str(error))
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unable to find user") from error
