import pythonds.basic
from pythonds.basic.stack import *

s = Stack()
class function_generator:

    def AND(self, outp, a, b):
        s.push(outp + "=" + a + "*" + b)


    def OR(self, outp, a, b):
        s.push(outp + "=" + a + "+" + b + "-" + a + "*" + b)


    def NOR(self, outp, a, b):
        s.push(outp + "=" + "1" + "+" + a + "*" + b + "-(" + a + "+" + b + ")")

    def XOR(self, outp, a, b):
        s.push(outp + "=" + a + "+" + b + "-" + "2" + "*" + a + "*" + b)

    def XNOR(self, outp, a, b):
        s.push(outp + "=" + "1" + "+" + "2" + "*" + a + "*" + b + "-(" + a + "+" + b + ")")

    def MUX(self, outp, a, b, c):
        if (c == 0.5):
            s.push(outp + "=" + "(" + a + "+" + b + ") / 2")


    def NOT(self, outp, a):
        s.push(outp + "=" + "1" + "-" + a)

    def NAND(self, outp, a, b):
        s.push(outp + "=" + "1" + "-" + a + "*" + b)


    def circuit_function(self):                   ##function calculator for stochastic circuit
        pop_list = []
        while (s.isEmpty() == False):
            pop_list.append(s.pop())
        ##print(pop_list)
        out_str = pop_list[0]
        length = len(pop_list)
        i = 1
        while(i<length):
            if pop_list[i].find("=") != -1:
                j = pop_list[i].find("=")
            else:
                i = i + 1
                continue
            if pop_list[i][0:j] in pop_list[0]:
                out_str = pop_list[0].replace(pop_list[i][0:j], pop_list[i][j+1:])
                pop_list[0] = out_str
                ##print(out_str)                     ##Stack implementation for backward calculation
            i = i + 1
        return out_str


    def circuit_maker(self):
        file_ptr = open("circuit_description.txt")
        while file_ptr:
            read_line = file_ptr.readline()
            if "AND" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("AND", "")
                line_parser = line_parser.replace(" ", "")
                self.AND(line_parser[0:2], line_parser[2:4], line_parser[4:6])
                continue;

            if "MUX" in read_line:
                line_parser = read_line
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("MUX", "")
                line_parser = line_parser.replace(" ", "")
                self.MUX(line_parser[0:2], line_parser[2:4], line_parser[4:6], 0.5)
                continue;


            if "OR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("OR", "")
                line_parser = line_parser.replace(" ", "")
                self.OR(line_parser[0:2], line_parser[2:4], line_parser[4:6])
                continue;

            if "NAND" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("NAND", "")
                line_parser = line_parser.replace(" ", "")
                self.NAND(line_parser[0:2], line_parser[2:4], line_parser[4:6])
                continue;

            if "NOR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("NOR", "")
                line_parser = line_parser.replace(" ", "")
                self.NOR(line_parser[0:2], line_parser[2:4], line_parser[4:6])
                continue;

            if "XOR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("XOR", "")
                line_parser = line_parser.replace(" ", "")
                self.XOR(line_parser[0:2], line_parser[2:4], line_parser[4:6])
                continue;

            if "XNOR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("XNOR", "")
                line_parser = line_parser.replace(" ", "")
                self.XNOR(line_parser[0:2], line_parser[2:4], line_parser[4:6])
                continue;

            if "NOT" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("NOT", "")
                line_parser = line_parser.replace(" ", "")
                self.NOT(line_parser[0:2], line_parser[2:4])
                continue;

            if "END" in read_line:
                file_ptr.close()
                break;



        funct_expr = self.circuit_function()
        print (funct_expr)
        return funct_expr

