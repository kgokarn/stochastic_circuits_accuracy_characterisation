import numpy as np

class circuit_simulation:
    def circuit(self, slength, circuit_simulation_list):
        input_output_dictionary = {}                                     #Inputs read from file are maintained in dictionary
        input_read_line = open("input.txt")

        while input_read_line:
            input_line = input_read_line.readline()
            if "=" in input_line:
                input_parser = input_line
                input_parser = input_parser.strip(" ")
                input_parser = input_parser.replace(" ", "")
                input_parser = input_parser.split("=")
                input_parser[1] = input_parser[1].rstrip("\n")
                input_parser[1] = self.SNG(float(input_parser[1]), slength)
                input_output_dictionary[input_parser[0]] = input_parser[1]

            if "END" in input_line:
                input_read_line.close()
                break;


        ckt_ptr = open("circuit_description.txt")                          #Circuit read from the file for simulation
        while ckt_ptr:
            read_line = ckt_ptr.readline()
            if "AND" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("AND", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.AND(input_output_dictionary.get(line_parser[2:4]), input_output_dictionary.get(line_parser[4:6]))
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "MUX" in read_line:
                line_parser = read_line
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("MUX", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.MUX(input_output_dictionary.get(line_parser[2:4]), input_output_dictionary.get(line_parser[4:6]), 0.5, slength)
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "OR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("OR", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.OR(input_output_dictionary.get(line_parser[2:4]), input_output_dictionary.get(line_parser[4:6]))
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "NAND" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("NAND", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.NAND(input_output_dictionary.get(line_parser[2:4]), input_output_dictionary.get(line_parser[4:6]))
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "NOR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("NOR", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.NOR(input_output_dictionary.get(line_parser[2:4]), input_output_dictionary.get(line_parser[4:6]))
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "XOR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("XOR", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.XOR(input_output_dictionary.get(line_parser[2:4]), input_output_dictionary.get(line_parser[4:6]))
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "XNOR" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("XNOR", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.XNOR(input_output_dictionary.get(line_parser[2:4]), input_output_dictionary.get(line_parser[4:6]))
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "NOT" in read_line:
                line_parser = read_line
                line_parser = line_parser.strip(" ")
                line_parser = line_parser.replace(",", "")
                line_parser = line_parser.replace("(", "")
                line_parser = line_parser.replace(")", "")
                line_parser = line_parser.replace("NOT", "")
                line_parser = line_parser.replace(" ", "")
                line_parser_temp = self.NOT(input_output_dictionary.get(line_parser[2:4]))
                input_output_dictionary[line_parser[0:2]] = line_parser_temp
                computed_output = line_parser_temp
                continue;

            if "END" in read_line:
                ckt_ptr.close()
                break;

        stoc_output = self.COUNT(computed_output, slength)
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

    def mean_square_error(self, theoretical, simulation):                   #Calculation of Mean Square Error
        input_read_line = open("input.txt")
        probablity_input_output_dictionary = {}
        variable_dictionary = {}
        variable_count = 0
        while input_read_line:                                              #Input file parsing for theortical output value
            input_line = input_read_line.readline()
            if "=" in input_line:
                input_parser = input_line
                input_parser = input_parser.strip(" ")
                input_parser = input_parser.replace(" ", "")
                input_parser = input_parser.split("=")
                input_parser[1] = input_parser[1].rstrip("\n")
                variable_count = variable_count + 1
                probablity_input_output_dictionary[input_parser[0]] = input_parser[1]

            if "END" in input_line:
                input_read_line.close()
                break

        for x in range(variable_count):
            new_variable_name = "i" + str(x + 1)
            globals()['i%s' % (x+1)] = float(probablity_input_output_dictionary.get(new_variable_name))

        #i1 = i2 = i3 = i4 = i5= i6 = 0.5
        i = 0
        j = 0
        sum = 0
        mse_list = []
        if theoretical.find("=") != -1:
            j = theoretical.find("=")

        theoretical_rhs = theoretical[j+1:]
        theoretical_value = (eval(theoretical_rhs))
        print("theoretical value = ", theoretical_value)

        while(i < len(simulation)):
            mse_list.append((theoretical_value - simulation[i])**2)
            i = i + 1
        print(mse_list)

        while(j < len(mse_list)):
            sum = sum + mse_list[j]
            j = j + 1

        mean_square_error = sum / len(mse_list)
        return mean_square_error











