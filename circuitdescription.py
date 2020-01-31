import pythonds.basic
from pythonds.basic.stack import *

s = Stack()
class function_generator:

    def AND(self, outp, a, b):
        s.push(outp + "=" + a + "*" + b)


    def OR(self, outp, a, b):
        s.push(outp + "=" + a + "+" + b)


    def NOR(self, a, b):
        if (a == True):
            return False
        elif (b == True):
            return False
        else:
            return True

    def XOR(self, outp, a, b):
        s.push(outp + "=" + a + "+" + b)

    def XNOR(self, outp, a, b):
        s.push(outp + "=" + a + "~" + b)

    def MUX(self, outp, a, b, c):
        if (c == 0.5):
            s.push(outp + "=" + "(" + a + "+" + b + ") / 2")


    def NOT(self, outp, a):
        s.push(outp + "=" + "1" - "a")

    def NAND(self, a, b):
        if ((a == True) and (b == True)):
            return False
        else:
            return True

    def circuit_function(self):                   ##function calculator for stochastic circuit
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
                print(out_str)                     ##Stack implementation for backward calculation
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

