"""
Views for the Accounts app are interfaces to use cases dealing with content manipulation.

View functions are what we might consider user-facing HTTP adapters. We avoid putting any business
logic here, but also avoid reliance on Django models. They are in charge of validating user input,
formatting responses, and routing the requests to use cases.
"""

import json

from django.http import JsonResponse

from adapters.django_storage import DjangoStorage
from .use_cases import AccountUseCases

use_cases = AccountUseCases(DjangoStorage())


def create_account(request):
    """Create new user account with name, email, password submitted by user."""
    req_data = json.loads(request.body.decode('utf8'))
    try:
        name = req_data['name']
        email = req_data['email']
        password = req_data['password']
    except KeyError as e:
        return JsonResponse(
            {
                'success': False,
                'message': 'Missing required key {}'.format(e)
            },
            status=400
        )

    user = use_cases.create_account(user_dict={'name': name, 'email': email}, password=password)

    return JsonResponse({'user': user.asdict()})
