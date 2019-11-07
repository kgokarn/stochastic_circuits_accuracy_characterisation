import pythonds.basic
from pythonds.basic.stack import *


class function_generator:
    s = Stack()

    def AND(self, a, b):
        s.push(a * b)
        if ((a == True) and (b == True)):
            return True
        else:
            return False

    def OR(self, a, b):
        if (a == True):
            return True
        elif (b == True):
            return True
        else:
            return False

    def NOR(self, a, b):
        if (a == True):
            return False
        elif (b == True):
            return False
        else:
            return True

    def XOR(self, a, b):
        if (a != b):
            return True
        else:
            return False

    def XNOR(self, a, b):
        if (a == b):
            return True
        else:
            return False

    def MUX(self, a, b, c):
        if (c == 0.5):
            s.push((a + b) / 2)

        if (c == 1):
            return a
        else:
            return b

    def NOT(self, a):
        if (a == True):
            return False
        else:
            return True

    def NAND(self, a, b):
        if ((a == True) and (b == True)):
            return False
        else:
            return True

    def circuit_maker(self):
        i1 = i2 = i3 = i4 = i5 = i6 = False
        a1 = self.AND(i1, i2)
        a2 = self.AND(i3, i4)
        a3 = self.AND(i5, i6)
        m1 = self.MUX(a1, a2, 0.5)
        m2 = self.MUX(m1, a3, 0.5)
