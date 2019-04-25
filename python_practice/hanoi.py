import math

class Ring:
    def __init__(self,value):
        self.value = value

    def re_value(self):
        return self.value

class Bar:
    def __init__(self):
        self.rings = []

    def set_ring(self,ring)
        self.rings.append(ring)

    def is_empty(self):
        return self.rings == []

class Hanoi:
    def __init__(self,bar_value,ring_value):
        self.rings = set_rings(ring_value)
        self.bars = set_bars(bar,self.rings)

    def set_rings(self,value):
        rings = []
        for i in range(value):
            rings.append(Ring(i))
        return rings

    def set_bars(self,value,rings):
        bars = []
        for i in range(values):
            bars.append(Bars())
        for j in range(len[rings]):
            bars[0].set_bars(rings[j])
        return bars

def solve(hanoi):

def main():
    The_Hanoi = Hanoi(3,3)
    solve(The_Hanoi)

if __name__ == "__main__":
    main()