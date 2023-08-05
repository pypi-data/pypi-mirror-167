""" User Population Get Controller Definition """

from rowantree.contracts import UserPopulation

from .abstract_controller import AbstractController


class UserPopulationGetController(AbstractController):
    """
    User Population Get Controller
    Gets the user population.

    Methods
    -------
    execute(self, user_guid: str) -> UserPopulation
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserPopulation:
        """
        Gets the user population.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_population: UserPopulation
            User population object.
        """

        return self.dao.user_population_by_guid_get(user_guid=user_guid)
