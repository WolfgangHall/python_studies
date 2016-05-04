#want to accept an arbitrary number of arguments but
# you won't know ahead of time what kind of info will be passed to the function

#build_profile() expects a first and last name
# allows the user to pass in as many name-value pairs as they want
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton')
print(user_profile)