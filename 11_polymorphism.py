from item import Item

item1 = Item("MyItem", 750)

#POLYMORPHISM
'''
poly = many
morphism = form

Not a class level principle, but programming in general: Polymorphism = many forms. Single entity that knows how to handle different kinds of object.

Polymorphism in Action:
function len()
> a single function that knows how to handle different kind of objects as expected!

Polymorphism in OOP:
one function/method can handle multiple kind of objects (classes) by virtue of inheritance

Example:  apply_discount() can handle both Item objects and Phone objects
So in OOP it's just an extension of the inheritance principle
'''