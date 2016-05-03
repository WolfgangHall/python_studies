user_0 = {
    'username' : 'wolfgang7',
    'first': 'john',
    'last': 'hall'
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# for k, v in user_0.items()
#items() returns a list of key-value pairs
#we can choose any names we want for key and value

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#can use sorted() function to get a copy of keys in order
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")