""" World Status Get Controller Definition """

from rowantree.contracts import WorldStatus

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

    def execute(self) -> WorldStatus:
        """
        Gets the world status.

        Returns
        -------
        world_status: WorldStatus
            The world status.
        """

        return WorldStatus(active_players=self.dao.users_active_get())
