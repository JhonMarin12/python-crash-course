def build_profile(first, last, **user_info):
    """Build a dictionary containing everithing we know about user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Albert',
                            'Einstein',
                            field = 'Physics'
                            )
print(user_profile)