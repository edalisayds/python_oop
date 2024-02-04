from item import Item
from phone import Phone

item1 = Item("MyItem", 750)

print(item1.name)
print(item1._name) #it's not a good python practice to put underscore when accessing attributes when calling instance but it works just as fine. Underscores are usually used in class level
print(item1.read_only_name)

