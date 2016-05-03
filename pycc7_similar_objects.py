#can also use a dictionary to store one kind of info about many objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# print("Sarah's favorite language is " + 
#     favorite_languages['sarah'].title() +
#     ".")

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + 
        language.title() + 
        ".")


#keys() method can be used for one value
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favorite language is " +
#you can use the name of the dictionary and current value of name as the key
            favorite_languages[name].title() + "!")


