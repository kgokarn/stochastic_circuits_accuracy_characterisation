import math

class accuarcy_characterization:
    def calc_stochastic_number(self, conf_level, err_tolerance, mean_square_error):
        return math.ceil(mean_square_error/((1 - conf_level)* pow(err_tolerance, 2)))

    def calc_error_tolerance(self, conf_level, stoc_number, mean_square_error):
        return math.sqrt(mean_square_error)/(math.sqrt(stoc_number * (1 - conf_level)))

    def calc_confidence_level(self, err_tolerance, stoc_number, mean_square_error):
        return 1 - (mean_square_error/(stoc_number * pow(err_tolerance, 2)))

