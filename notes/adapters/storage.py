import abc

from common.exception import DoesNotExist


class Storage(abc.ABC):
    DoesNotExist = DoesNotExist

    # ----
    # note
    # ----

    @abc.abstractmethod
    def save_note(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_note(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete_note(self, *args, **kwargs):
        pass

    # -----
    # board
    # -----

    @abc.abstractmethod
    def get_board(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def save_board(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete_board(self, *args, **kwargs):
        pass

    # ----------
    # board user
    # ----------

    @abc.abstractmethod
    def save_board_user(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_board_notes(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def get_board_users(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def delete_board_user(self, *args, **kwargs):
        pass
