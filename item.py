import csv


class Item:
    pay_rate = 0.8 # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        #Run validations to received arguments
        assert price    >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        #Assign to self object
        #Double underscore means that the attributes is only accessible on class level, outside of class it's not allowed to be used
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)

    @property
    def name(self):
        return self.__name
    '''
    Property Decorator = Read-Only Attribute
    Hence, below block of code is illegal 
    because then it would not allow the the name to be initialized in def __init__ when self.name is instantiated

    def __init__(self, name: str):
        self.name = name

    @property
    def name(self):
        return self.name 
    '''

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        '''
        how to access class level attribute:
        self.price = self.price * Item.pay_rate
        this ^ method will always just utilize the "Item" class level attribute pay_rate
        in order to allow both the class level and overriden instance level attribute pay_rate
        we use instead self.pay_rate, hence:
        '''
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        '''
        class method should also do something with that has a relationship to the class,
        but usually, these are used to manipulate different structures of data (ie csv, json, yaml etc) to instantiate
        objects, like below for csv

        main difference between a class and static method is that static methods are not passing the method as first argument,
        static methods work like regular python function
        '''
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            # instantiate the objects
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        '''
        static method are much like regular functions,
        no longer need to pass through the object "self" itself

        This should do something that has a relationship with the class,
        but not something that must be unique per instance
        '''
        if isinstance(num, float):
            #this is a little confusing except for the fact that there's a built it is_integer() function in python
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.name}\", {self.price}, {self.quantity})"

    @property
    def read_only_name(self):
        return "AAA"