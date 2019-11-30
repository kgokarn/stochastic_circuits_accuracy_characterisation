import pythonds.basic
from pythonds.basic.stack import *

s = Stack()
class function_generator:

    def AND(self, outp, a, b):
        s.push(outp + "=" + a + "*" + b)
        #if ((a == True) and (b == True)):
        #    return True
        #else:
        #    return False

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

    def MUX(self, outp, a, b, c):
        if (c == 0.5):
            s.push(outp + "=" + "(" + a + "+" + b + ") / 2")

        #if (c == 1):
        #   return a
        #else:
        #    return b

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

    def circuit_function(self):
        pop_list = []
        while (s.isEmpty() == False):
            pop_list.append(s.pop())
        print(pop_list)
        out_str = pop_list[0]
        length = len(pop_list)
        i = 1
        while(i<length):
            if pop_list[i].find("=") != -1:
                j = pop_list[i].find("=");
            else:
                i = i + 1
                continue
            if pop_list[i][0:j] in pop_list[0]:
                out_str = pop_list[0].replace(pop_list[i][0:j], pop_list[i][j+1:])
                pop_list[0] = out_str
                print(out_str)
            i = i + 1
        print(out_str)










    def circuit_maker(self):
        #i1 = i2 = i3 = i4 = i5 = i6 = False
        self.AND("a1","i1", "i2")
        self.AND("a2","i3", "i4")
        self.AND("a3","i5", "i6")
        self.MUX("m1","a1", "a2", 0.5)
        self.MUX("m2","m1", "a3", 0.5)
        self.circuit_function()

