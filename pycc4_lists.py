bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#0 index of list is first
print(bicycles[0])

#can use string methods on list items
print(bicycles[0].title())

#returns last element in list
print(bicycles[-1])

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)