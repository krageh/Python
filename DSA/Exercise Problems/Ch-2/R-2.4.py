class Flower(object):
    def __init__ (self, name, petals, price):
        self.name = name
        self.petals = petals
        self.price = price

    def get_name(self):
        return self.name
    
    def get_petals(self):
        return self.petals
    
    def get_price(self):
        return self.price

    def set_name(self, newname):
        self.name = newname

    def set_petals(self, newnumber):
        self.petals = newnumber

    def set_price(self, newprice):
        self.price = newprice