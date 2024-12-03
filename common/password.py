from passlib.hash import django_pbkdf2_sha256


def generate_password(password):
    """
    Hashes and sets a user's password
    """

    hashed_password = django_pbkdf2_sha256.hash(password)
    print('hashed_password-->', hashed_password)
    return hashed_password


def verify_password(password, hashed_password):
    """
    Checks if a password matches a given hash

    This method is for converting django password

    """
    # print(django_pbkdf2_sha256.verify(password, hashed_password))

    if django_pbkdf2_sha256.verify(password, hashed_password):
        return True
    else:
        return False


"""
    ---------- 1 ------------

    is_valid_password = pbkdf2_sha256.verify(password, hashed_password)

    if is_valid_password:
        print('Password is valid')
    else:
        print('Password is invalid')

    Throwing  ValueError: not a valid pbkdf2_sha256 hash
    """

"""
--------- 2 ---------

if bcrypt.checkpw(password.encode(), hashed_password.encode()):
     print('Password is valid')
else:
    print('Password is invalid')

Throwing Salt Error
"""

"""
------------ 3 ------------

_, salt, _ = hashed_password.split('$', 2)


known_salt = bcrypt.gensalt()

salted_password = known_salt + password.encode()
known_hash = bcrypt.hashpw(salted_password, known_salt)


print("known_hash.decode()", known_hash.decode())
print("hashed_password", hashed_password)
if known_hash.decode() == hashed_password:
    print('Password is valid')
else:
    print('Password is invalid')

Not Matching 
"""
