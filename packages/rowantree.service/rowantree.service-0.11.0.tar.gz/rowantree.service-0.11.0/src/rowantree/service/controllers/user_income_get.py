""" User Income Get Controller Definition """

from rowantree.contracts import UserIncomes

from .abstract_controller import AbstractController


class UserIncomeGetController(AbstractController):
    """
    User Income Get Controller
    Gets (unique) list of user incomes.

    Methods
    -------
    execute(self, user_guid: str) -> UserIncomes
        Executes the command.
    """

    def execute(self, user_guid: str) -> UserIncomes:
        """
        Gets (unique) list of user incomes.

        Parameters
        ----------
        user_guid: str
            The target user guid.

        Returns
        -------
        user_incomes: UserIncomes
            A (unique) list of user incomes.
        """

        return self.dao.user_income_get(user_guid=user_guid)
