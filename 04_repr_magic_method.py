class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []
    def __init__(self, name:str, price:float, quantity=0):
        #Run validations to received arguments
        assert price    >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        #how to access class level attribute:
        #self.price = self.price * Item.pay_rate
        #this ^ method will always just utilize the "Item" class level attribute pay_rate
        #in order to allow both the class level and overriden instance level attribute pay_rate
        #we use instead self.pay_rate, hence:
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item(\"{self.name}\", {self.price}, {self.quantity})"

item1 = Item("Phone", 100,1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print("\nList down the Items")
#without the __repr__ magic method, the list will be shown as object ids, representing each initialized object
print(Item.all)

print("\nList down the name of the Items")
for i in Item.all:
    print(i.name)

