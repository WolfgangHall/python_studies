name = "wolfgang hall"
print(name.title())

print(name.upper())
print(name.lower())

first_name = "faye"
last_name = "valentine"
full_name = first_name + " " + last_name
print(full_name)

message = "Hello, " + full_name.title() + "!"
print(message)

#adding whitespaces to strings with tabs
print ("Python")
print("\tPython")

#adding a newline
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#stripping whitespace
favorite_language = 'english '
favorite_language.rstrip() #would by 'python'
#However it is only removed temporarily
#You must store stripped value in a variable
favorite_language.lstrip()
favorite_language.strip()