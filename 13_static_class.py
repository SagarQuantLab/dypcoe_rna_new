class College:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def my_public_method(self):
        return f"{self.a}, {self.b}"
    
    @staticmethod
    def my_static_method(a, b):
        return f"{a}, {b}"
    
    def addition(self):
        return self.a + self.b
    

class TCS:

    def fetch_public_method(self):
        collegeIns = College(2, 3)
        a = collegeIns.my_public_method()
        print(a)
        return collegeIns.addition()

class WIPRO:

    def fetch_static_method(self):
        College.my_static_method(4, 5)
        return College.addition()



tcsIns = TCS()
print(tcsIns.fetch_public_method())
wiproIns = WIPRO()
print(wiproIns.fetch_static_method())
