from abc import ABC, abstractmethod

class govt(ABC):

    @abstractmethod
    def get_your_license(self):
        pass

class govt(govt):

    def get_your_license(self):
        return "yes I applied for license"

class pizzShop(govt):

    def __init__(self, owner_name, owner_age):
        self.owner_name = owner_name
        self.owner_age = owner_age

    def get_your_license(self):
        return f"Yes I got my license - {self.owner_name}"

pIns = pizzShop('Rohan', 35)
print(pIns.owner_name, pIns.owner_age)
print(pIns.get_your_license())

gIns = govt()
print(gIns.get_your_license())