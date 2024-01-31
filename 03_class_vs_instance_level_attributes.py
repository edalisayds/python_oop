class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations to received arguments
        assert price    >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        #how to access class level attribute:
        #self.price = self.price * Item.pay_rate
        #this ^ method will always just utilize the "Item" class level attribute pay_rate
        #in order to allow both the class level and overriden instance level attribute pay_rate
        #we use instead self.pay_rate, hence:
        self.price = self.price * self.pay_rate


item1 = Item("Phone", 100,5)
item2 = Item("Laptop", 1000, 3)

#overriding class level attribute with instance level attribute
item2.pay_rate = 0.7

print("\nClass vs Instance level Pay Rate Attribute")
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

print("\nClass vs Instance level attribute dictionary")
print(Item.__dict__)
print(item1.__dict__)


print("\nOverriding class level attribute and its use cases")
item1.apply_discount()
print(item1.price)

item2.apply_discount()
print(item2.price)