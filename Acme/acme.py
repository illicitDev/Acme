"""Create Product class for ACME Corporation"""
import random as rnd


class Product:
    """Product Class"""
    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammability=0.5,
        identifier=rnd.randint(1000000, 10000000)):

        self.name = str(name)
        self.price = int(price)
        self.weight = int(weight)
        self.flammability = float(flammability)
        self.identifier = int(identifier)

    def __repr__(self):
        
        return f'{self.name}, {self.price}, {self.weight}, {self.flammability}'

    def stealability(self):
        """Compute stealability"""
        stealability = self.price / self.weight

        if stealability < 0.5:
            return 'Not so stealable...'
        elif stealability >= 0.5 and stealability < 1:
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """Compute explosiveness"""
        explode = self.flammability * self.weight

        if explode < 10:
            return '...fizzle.'
        elif explode >= 10 and explode < 50:
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """Boxing Glove object that inherits from Product"""
    def __init__(
        self,
        name,
        price=10,
        weight=10,
        flammability=0.5,
        identifier=rnd.randint(1000000, 10000000)):

        super().__init__(name=str(name), price=int(price),
                         weight=int(weight),
                         flammability=float(flammability),
                         identifier=int(identifier))

    def explode(self):
        """Override explode method"""
        return '...it\'s a glove.'

    def punch(self):
        """Punch User"""
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight >= 5 and self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
