from accounts import models as accounts_models
from accounts.adapters.storage import Storage


class DjangoStorage(Storage):
    def create_user(self, user, password):
        """Create user entity.

        Because Django provides password hashing functionality that we want to use, we perform this
        action in the adapter, so that nothing is imported from Django in our use case.
        """
        django_user = accounts_models.User.objects.from_entity(user)
        django_user.set_password(password)
        django_user.save()
        return django_user.to_entity()
