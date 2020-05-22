import sys
import os
import os.path

sys.path.append('/home/kartik/PycharmProjects/SC/venv/bipolar_circuitdescription')
sys.path.append('/home/kartik/PycharmProjects/SC/venv/bipolar_simulation')
sys.path.append('/home/kartik/PycharmProjects/SC/venv/bipolar_accuracy')

from bipolar_circuitdescription import *
from bipolar_simulation import*
from bipolar_accuracy import*
#objects are created for python classes.
#objects for circuit identification, simulation and accuracy
fun_gen = function_generator()
function_expression = fun_gen.circuit_maker()
continuous_simulation = circuit_simulation()
acc_char = accuarcy_characterization()



#To choose from either of the combinations
print ("1 : Confidence Level and Precision is given\n"
       "2 : Confidence Level and length of Stochastic Number is given\n"
       "3 : Precision and length of Stochastic Number is given\n")

given_choice = input("Enter the option that is given: ")

num_simulation = input("Enter the number of times the circuit needs to run: ")
circuit_simulation_list = []
ckt_trav_index = 0

if(given_choice == '1'):
    snumber = 32;                                                          ##Default Stochastic Number chosen to be 32
    conf_level = float(input("Enter the confidence level: "))
    precision = float(input("Enter the precision: "))
    while (ckt_trav_index <= int(num_simulation) - 1):
        circuit_simulation_list = continuous_simulation.circuit(snumber, circuit_simulation_list)
        ckt_trav_index = ckt_trav_index + 1
    print("circuit simulation result is: ",circuit_simulation_list)
    mean_square_error = continuous_simulation.mean_square_error(function_expression, circuit_simulation_list)
    print("Mean Square Error is: ", mean_square_error)
    stoc_number = acc_char.calc_stochastic_number(conf_level, precision, mean_square_error, num_simulation)
    print("optimal length of stochastic number is: ", stoc_number)

elif(given_choice == '2'):
    conf_level = float(input("Enter the confidence level: "))
    stoc_number = float(input("Enter the length of stochastic number: "))
    snumber = int(stoc_number);
    while (ckt_trav_index <= int(num_simulation) - 1):
        circuit_simulation_list = continuous_simulation.circuit(snumber, circuit_simulation_list)
        ckt_trav_index = ckt_trav_index + 1
    print("circuit simulation result is: ",circuit_simulation_list)
    mean_square_error = continuous_simulation.mean_square_error(function_expression, circuit_simulation_list)
    print("Mean Square Error is: ", mean_square_error)
    precision = acc_char.calc_precision(conf_level, stoc_number, mean_square_error, num_simulation)
    print("precision is: ", precision)

elif(given_choice == '3'):
    precision = float(input("Enter the precision: "))
    stoc_number = float(input("Enter the length of stochastic number: "))
    snumber = int(stoc_number);
    while (ckt_trav_index <= int(num_simulation) - 1):
        circuit_simulation_list = continuous_simulation.circuit(snumber, circuit_simulation_list)
        ckt_trav_index = ckt_trav_index + 1
    print("circuit simulation result is: ",circuit_simulation_list)
    mean_square_error = continuous_simulation.mean_square_error(function_expression, circuit_simulation_list)
    print("Mean Square Error is: ", mean_square_error)
    conf_level = acc_char.calc_confidence_level(precision, stoc_number, mean_square_error, num_simulation)
    print("confidence level is: ", conf_level)

else:
    print("Run the code again and pick a specified option")

