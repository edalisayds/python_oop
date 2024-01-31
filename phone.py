from item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #Run validations to received arguments
        #super is used to inherit full access of all the attributes and methods of the parent class
        super().__init__(name, quantity, price)
        assert broken_phones >= 0, f"Quantity {broken_phones} is not greater than or equal to zero!"

        #Assign to self object
        self.broken_phones = broken_phones