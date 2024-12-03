import os

from v1.users import queryset as auth_queryset


def generate_key():
    import binascii
    return binascii.hexlify(os.urandom(20)).decode()


def create_token(user_id):
    token_exists = auth_queryset.get_token({'user': user_id})
    if token_exists:
        token = token_exists['key']
    else:

        data = {
            'key': str(generate_key()),
            'user': user_id,
        }
        token = auth_queryset.insert_token(data)
        token = token.key

    return token
