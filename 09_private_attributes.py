from item import Item
from phone import Phone

item1 = Item("MyItem", 750)

print(item1.read_only_name)
#cannot override value for this one
#eg: item1.read_only_name = "BBB" would throw an error

print(item1.name)
'''
there's a completely new concept that handles ^ that altogether: 
which is the use of double underscores for attributes within the class
this makes the attributes "private" and inaccessible OUTSIDE the class

eg: below would throw an error
print(item1.__name)
'''
