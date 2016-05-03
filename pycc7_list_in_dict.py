pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) == 2:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())