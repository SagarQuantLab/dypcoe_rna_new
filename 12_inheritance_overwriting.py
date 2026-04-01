class maths:

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def _addition(self):
        return self.second_num + self.first_num
    
class childMaths(maths):

    def __init__(self, first_num, second_num):
        maths.__init__(self, first_num, second_num)

    def addition(self):
        return self.first_num * self.second_num
    

a = childMaths(2, 3)
print(a.addition())
print(a._addition())