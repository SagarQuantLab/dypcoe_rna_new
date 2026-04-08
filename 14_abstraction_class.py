from abc import ABC, abstractmethod

class college(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def follow_dress_code(self):
        pass
    
class A(college):

    def __init__(self, name):
        college.__init__(self, name)
    
    def follow_dress_code(self):
        return f"yes I am following {self.name}"

class S(college):

    def my_name(self, name):
        self.name = name

    def follow_dress_code(self):
        return f"yes I am following {self.name}"
    
aIns = A('Neha')
print(aIns.follow_dress_code())

sIns = S('Neha')
sIns.my_name('Sanjana')
print(sIns.follow_dress_code())

    