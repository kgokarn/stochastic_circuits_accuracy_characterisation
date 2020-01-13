import math

class accuarcy_characterization:
    def calc_stochastic_number(self, conf_level, err_tolerance):
        return math.ceil(9/(conf_level* pow(err_tolerance, 2)))

    def calc_error_tolerance(self, conf_level, stoc_number):
        return 3/(math.sqrt(stoc_number * conf_level))

    def calc_confidence_level(self, err_tolerance, stoc_number):
        return 9/(stoc_number * pow(err_tolerance, 2))

