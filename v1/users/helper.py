from v1.referral import queryset as referral_queryset
from v1.users import queryset as users_queryset
from v1.users.constants import REFERRAL_TYPE_BOTH_USER, REFERRAL_TYPE_FROM_USER, REFERRAL_TYPE_TO_USER


def update_or_insert_wallet(user_id, amount, existing_wallet):
    if existing_wallet:
        wallet_amount = existing_wallet.get('wallet_amount', 0) + amount
        users_queryset.update_user_wallet({'user_id': user_id}, {'wallet_amount': wallet_amount})
    else:
        users_queryset.insert_user_wallet({'user_id': user_id, 'wallet_amount': amount})

    return True

def add_referral(referral_code, to_user_id):
    active_referral_object = referral_queryset.get_referral_data({"is_active": True})
    from_user = users_queryset.get_data({'referral_code': referral_code})

    if not active_referral_object or not from_user:
        return True

    from_user_id = from_user.get('user_id')
    referral_type = active_referral_object.get('referral_type', '')

    # Referral amounts for both users
    from_user_amount = active_referral_object.get('from_user_referral_amount', 0)
    to_user_amount = active_referral_object.get('to_user_referral_amount', 0)

    # Get user wallets once
    from_user_wallet = users_queryset.get_user_wallet({'user_id': from_user_id})
    to_user_wallet = users_queryset.get_user_wallet({'user_id': to_user_id})

    if referral_type == REFERRAL_TYPE_BOTH_USER:
        update_or_insert_wallet(from_user_id, from_user_amount, from_user_wallet)
        update_or_insert_wallet(to_user_id, to_user_amount, to_user_wallet)

    elif referral_type == REFERRAL_TYPE_FROM_USER:
        update_or_insert_wallet(from_user_id, from_user_amount, from_user_wallet)

    elif referral_type == REFERRAL_TYPE_TO_USER:
        update_or_insert_wallet(to_user_id, to_user_amount, to_user_wallet)

    return True
