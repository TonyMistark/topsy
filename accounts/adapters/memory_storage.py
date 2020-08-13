from .storage import Storage


class MemoryStorage(Storage):
    """Adapter to use system memory as a storage backend."""

    def __init__(self):
        """Setup dictionaries as stores for each entity type."""
        self.users = {}

    def create_user(self, user, password):
        """Create user entity."""
        if user.id is None:
            existing_ids = self.users.keys()
            new_id = 1 if len(existing_ids) == 0 else max(existing_ids) + 1
            # user = user.replace(id=new_id)
            user = user.copy(update={id: new_id})

        self.users[user.id] = user
        return user

    def get_user(self, id):
        try:
            return self.users[id]
        except KeyError:
            raise self.DoesNotExist("User {} was not found".format(id))
