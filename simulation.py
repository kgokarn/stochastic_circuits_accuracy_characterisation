import numpy as np

class circuit_simulation:
    def circuit(self, slength, circuit_simulation_list):
        ##i1 = float(input("Enter the value for i1: "))
        ##i2 = float(input("Enter the value for i2: "))
        ##i3 = float(input("Enter the value for i3: "))
        ##i4 = float(input("Enter the value for i4: "))
        ##i5 = float(input("Enter the value for i5: "))
        ##i6 = float(input("Enter the value for i6: "))
        i1 = i2 = i3 = i4 = i5 = i6 = 0.5
        i1_sn = self.SNG(i1, slength)
        i2_sn = self.SNG(i2, slength)
        i3_sn = self.SNG(i3, slength)
        i4_sn = self.SNG(i4, slength)
        i5_sn = self.SNG(i5, slength)
        i6_sn = self.SNG(i6, slength)

        a1 = self.AND(i1_sn, i2_sn)
        a2 = self.AND(i3_sn, i4_sn)
        a3 = self.AND(i5_sn, i6_sn)
        m1 = self.MUX(a1, a2, 0.5, slength)
        m2 = self.MUX(m1, a3, 0.5, slength)
        stoc_output = self.COUNT(m2, slength)
        circuit_simulation_list.append(stoc_output)
        return circuit_simulation_list


    def SNG(self, bin_num, slength):                             ##Function for Stochastic Number Generator
        ran_num = np.random.uniform(size=slength)                ##Uniform Distribution is used for random SN generator
        stoc_bitstream = []
        i = 0
        while(i < slength):
            if bin_num > ran_num[i]:
                stoc_bitstream.append(True)
            else:
                stoc_bitstream.append(False)
            i = i + 1
        return stoc_bitstream

    def COUNT(self, a, slength):                                  ##Function of Counter implementation
        i = 0
        count = 0
        while(i < slength):
            if(a[i] == True):
                count = count + 1
            i = i + 1
        return count/slength


    def AND(self, a, b):
        i = 0
        c = []
        list_length = len(a)
        while (i < list_length):
            c.append(a[i] & b[i])
            i = i + 1
        return c

    def OR(self, a, b):
        i = 0
        c = []
        list_length = len(a)
        while (i < list_length):
            c.append(a[i] | b[i])
            i = i + 1
        return c

    def NOT(self, a):
        i = 0
        c = []
        list_length = len(a)
        while (i < list_length):
            c.append(~a[i])
            i = i + 1
        return c

    def XOR(self, a, b):
        i = 0
        c = []
        list_length = len(a)
        while (i < list_length):
            c.append(a[i] ^ b[i])
            i = i + 1
        return c

    def XNOR(self, a, b):
        i = 0
        c = []
        list_length = len(a)
        while (i < list_length):
            c.append(~(a[i] ^ b[i]))
            i = i + 1
        return c

    def NAND(self, a, b):
        i = 0
        c = []
        list_length = len(a)
        while (i < list_length):
            c.append(~(a[i] & b[i]))
            i = i + 1
        return c

    def NOR(self, a, b):
        i = 0
        c = []
        list_length = len(a)
        while (i < list_length):
            c.append(~(a[i] | b[i]))
            i = i + 1
        return c

    def MUX(self, a, b, c, slength):
        if (c == 0.5):
            c = self.SNG(c, slength)
            j = 0
            sum = []
            while(j < slength):
                if(c[j] == False):
                    sum.append(a[j])
                else:
                    sum.append(b[j])
                j = j + 1
        return sum

    def mean_square_error(self, theoretical, simulation):
        i1 = i2 = i3 = i4 = i5= i6 = 0.5
        i = 0
        j = 0
        sum = 0
        mse_list = []
        if theoretical.find("=") != -1:
            j = theoretical.find("=")

        theoretical_rhs = theoretical[j+1:]
        theoretical_value = (eval(theoretical_rhs))
        print(theoretical_value)

        while(i < len(simulation)):
            mse_list.append((theoretical_value - simulation[i])**2)
            i = i + 1
        print(mse_list)

        while(j < len(mse_list)):
            sum = sum + mse_list[j]
            j = j + 1

        mean_square_error = sum / len(mse_list)
        return mean_square_error











