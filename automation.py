import sys
import os
import os.path

sys.path.append('/home/kartik/PycharmProjects/SC/venv/circuitdescription')
sys.path.append('/home/kartik/PycharmProjects/SC/venv/simulation')
sys.path.append('/home/kartik/PycharmProjects/SC/venv/accuracy')

from circuitdescription import *
from simulation import*
from accuracy import*
fun_gen = function_generator()
function_expression = fun_gen.circuit_maker()
continuous_simulation = circuit_simulation()
acc_char = accuarcy_characterization()




print ("1 : Confidence Level and Error Tolerance is given\n"
       "2 : Confidence Level and Stochastic Number is given\n"
       "3 : Error Tolerance and Stochastic Number is given\n")

given_choice = input("Enter the option that is given: ")
print(given_choice)

num_simulation = input("Enter the number of times the circuit needs to run: ")
circuit_simulation_list = []
ckt_trav_index = 0

if(given_choice == '1'):
    snumber = 32;                                                          ##Default Stochastic Number chosen to be 32
    conf_level = float(input("Enter the confidence level: "))
    err_tolerance = float(input("Enter the error tolerance: "))
    while (ckt_trav_index <= int(num_simulation) - 1):
        circuit_simulation_list = continuous_simulation.circuit(snumber, circuit_simulation_list)
        ckt_trav_index = ckt_trav_index + 1
    print(circuit_simulation_list)
    ##continuous_simulation.mean_square_error(function_expression, circuit_simulation_list)
    stoc_number = acc_char.calc_stochastic_number(conf_level, err_tolerance)
    print("stochastic number is: ", stoc_number)

elif(given_choice == '2'):
    conf_level = float(input("Enter the confidence level: "))
    stoc_number = float(input("Enter the stochastic number: "))
    snumber = stoc_number;
    while (ckt_trav_index <= int(num_simulation) - 1):
        circuit_simulation_list = continuous_simulation.circuit(snumber, circuit_simulation_list)
        ckt_trav_index = ckt_trav_index + 1
    print(circuit_simulation_list)
    err_tolerance = acc_char.calc_error_tolerance(conf_level, stoc_number)
    print("error tolerance is: ", err_tolerance)

elif(given_choice == '3'):
    err_tolerance = float(input("Enter the error tolerance: "))
    stoc_number = float(input("Enter the stochastic number: "))
    snumber = stoc_number;
    while (ckt_trav_index <= int(num_simulation) - 1):
        circuit_simulation_list = continuous_simulation.circuit(snumber, circuit_simulation_list)
        ckt_trav_index = ckt_trav_index + 1
    print(circuit_simulation_list)
    conf_level = acc_char.calc_confidence_level(err_tolerance, stoc_number)
    print("confidence level is: ", conf_level)

else:
    print("Run the code again and pick a specified option")


