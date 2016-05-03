#using the 'in' keyword to check for value in list
requested_toppings = ['mushroooms', 'onions', 'pineapple']
print('mushroooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#using the 'not in' keyword to make sure value is not in list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")