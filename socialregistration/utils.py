import uuid

def generate_username(user, profile, client):
    """
    Default function to generate usernames using the built in `uuid` library.
    """
    return str(uuid.uuid4())[:30]


def generate_user(request, user, profile, client):
    """
    Default function to fill in user attributes
    """
    if hasattr(user, "username"):
        user.username = generate_username(user, profile, client)
    return user, profile
