""" World Status Get Controller Definition """
from rowantree.service.sdk import WorldStatusGetResponse

from ..controllers.abstract_controller import AbstractController


class WorldStatusGetController(AbstractController):
    """
    World Status Get Controller
    Gets the world status.

    Methods
    -------
    execute(self) -> WorldStatus
        Executes the command.
    """

    def execute(self) -> WorldStatusGetResponse:
        """
        Gets the world status.

        Returns
        -------
        world_status: WorldStatus
            The world status.
        """

        return WorldStatusGetResponse(active_users=self.dao.users_active_get())
