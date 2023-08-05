""" Abstract Controller Definition """

from abc import ABC, abstractmethod
from typing import Any, Optional

from ..services.db.dao import DBDAO


class AbstractController(ABC):
    """
    Abstract Controller

    Attributes
    ----------
    dao: DBDAO
        The database DAO.
    """

    dao: DBDAO

    def __init__(self, dao: DBDAO):
        self.dao = dao

    @abstractmethod
    def execute(self, *args, **kwargs) -> Optional[Any]:
        """Should be implemented in the subclass"""
