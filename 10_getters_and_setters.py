from item import Item
from phone import Phone

item1 = Item("MyItem", 750)
print(item1.name)
item1.name = "OtherItem"
print(item1.name)


#### ENCAPSULATION PRINCIPLE ####
'''
restricts the direct access of attributes in the class

Getters and setters are methods that provide controlled access and modification of private attributes. 
Getters = property decorators @property, retrieves the value of an attribute, 
Setters = @<attribute_name>.setter allow controlled modification, often including validation or additional logic. 

This encapsulation helps maintain data integrity, 
enhances code maintainability, 
and supports future modifications without affecting external code relying on the class interface. 
making it concise while adhering to the principles of encapsulation and abstraction.
'''