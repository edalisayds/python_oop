from item import Item
from phone import Phone

Item.instantiate_from_csv()
phone1 = Phone("jscPhonev10", 500, 5)
print(Item.all)