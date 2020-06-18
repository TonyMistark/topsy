import abc

from common.exception import DoesNotExist


class Storage(abc.ABC):
    DoesNotExist = DoesNotExist

    @abc.abstractmethod
    def create_user(self, *args, **kwargs):
        pass
