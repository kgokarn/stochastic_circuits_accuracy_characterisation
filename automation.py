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
fun_gen.circuit_maker()
mse_calc = circuit_simulation()
acc_char = accuarcy_characterization()




print ("1 : Confidence Level and Error Tolerance is given\n"
       "2 : Confidence Level and Stochastic Number is given\n"
       "3 : Error Tolerance and Stochastic Number is given\n")

given_choice = input("Enter the option that is given: ")
print(given_choice)

if(given_choice == '1'):
    snumber = 16;
    conf_level = float(input("Enter the confidence level: "))
    err_tolerance = float(input("Enter the error tolerance: "))
    mean_square_error = mse_calc.circuit(snumber)
    stoc_number = acc_char.calc_stochastic_number(conf_level, err_tolerance)
    print("stochastic number is: ", stoc_number)

elif(given_choice == '2'):
    conf_level = float(input("Enter the confidence level: "))
    stoc_number = float(input("Enter the stochastic number: "))
    snumber = stoc_number;
    mean_square_error = mse_calc.circuit(snumber)
    err_tolerance = acc_char.calc_error_tolerance(conf_level, stoc_number)
    print("error tolerance is: ", err_tolerance)

elif(given_choice == '3'):
    err_tolerance = float(input("Enter the error tolerance: "))
    stoc_number = float(input("Enter the stochastic number: "))
    snumber = stoc_number;
    mean_square_error = mse_calc.circuit(snumber)
    conf_level = acc_char.calc_confidence_level(err_tolerance, stoc_number)
    print("confidence level is: ", conf_level)

else:
    print("Run the code again and pick a specified option")


