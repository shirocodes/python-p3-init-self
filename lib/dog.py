#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed ='Mutt'):
        self.name = name
        self.breed = breed

    def bark(self):
        print('Woof!')

    def adopt(self, owner_name):
        self.owner = owner_name

fido = Dog('Fido', 'Bosco')
print(fido.name)
print(fido.breed)

fido.adopt('Sophie')
print(fido.owner)