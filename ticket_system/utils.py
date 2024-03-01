from django.contrib.auth.models import User


def create_user_with_password(username, role, firstname):
    password = generate_default_password(role, firstname)
    user = User.objects.create_user(username=username, password=password)
    return user

def generate_default_password(role, firstname):
    if role == 'User':
        return 'User@1234'
    else:
        return f'{firstname.capitalize()}@1234'
