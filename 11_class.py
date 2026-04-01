# class myclass:
#     pass

class grandma:

    def __init__(self, car, salary):
        self.grandma_car = car
        self.salary = salary

    def _access_grandma_car(self):
        return f"You can access my car {self.grandma_car} - from Grandma"

class grandpa:

    def __init__(self, car, salary):
        self.car = car
        self.salary = salary

    def _my_car_details(self):
        return f"You can drive my car {self.car} - from grandpa"
    
    def __my_salary(self):
        return f"You can't drive my car"
    
class papa(grandpa):

    def __init__(self, car, papa_salary, my_salary):
        self.my_salary = my_salary
        grandpa.__init__(self, car, papa_salary)

    def access_papa_car(self):
        return self._my_car_details()

    def access_papa_salary(self):
        return self.__my_salary()
    
    def __access_my_salary(self):
        return "You can't access my salary too"
    
class son(grandpa, grandma):

    def __init__(self, car, grandpa_salary, grandma_car, grandma_salary):
        grandpa.__init__(self, car, grandpa_salary)
        grandma.__init__(self, grandma_car, grandma_salary)

    def access_grandpa_car(self):
        return self._my_car_details()
    
    def access_grandma_car_child(self):
        return self._access_grandma_car()
    
    
# g = grandpa('Swift', 50000)
# print(g._my_car_details())

# p = papa('Swift', 50000, 80000)
# print(p.access_papa_car())
# print(p.access_papa_salary())

s = son('Swift', 50000, 'seltos', 80000)
print(s.access_grandpa_car())
print(s.access_grandma_car_child())