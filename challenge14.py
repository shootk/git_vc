#challenge14

#1
class Square:
    square_list = []
    
    def __init__(self,sides):
        self.sides = sides
        self.square_list.append(self)
#2
    def __repr__(self):
        rep = str(self.sides)
        for i in range(3):
            rep += " by {}".format(self.sides)
        return rep

#3
def comp(ob1,ob2):
    if ob1 is ob2:
        return True
    else:
        return False

sq1 = Square(3)
sq2 = Square(5)
sq3 = Square(4)

print(sq1.square_list)
print(sq1)
sq4 = sq1
sq5 = Square(3)
print(comp(sq1,sq4),comp(sq1,sq5))
