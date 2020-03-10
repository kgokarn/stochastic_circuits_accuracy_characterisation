import math
from scipy.stats import norm
#CLT relation between stochastic number, error tolernace and confidence level
class accuarcy_characterization:
    def calc_stochastic_number(self, conf_level, err_tolerance, mean_square_error, num_simulation):
        return math.ceil(math.pow(norm.ppf(norm.cdf((1 - (1 - conf_level)/2 ))) * math.sqrt(mean_square_error * int(num_simulation))/err_tolerance, 2))

    def calc_error_tolerance(self, conf_level, stoc_number, mean_square_error, num_simulation):
        return norm.ppf(norm.cdf((1 - (1 - conf_level)/2 ))) * math.sqrt((int(num_simulation) * mean_square_error)/stoc_number)

    def calc_confidence_level(self, err_tolerance, stoc_number, mean_square_error, num_simulation):
        return 2 * norm.cdf(math.sqrt((mean_square_error * int(num_simulation))/ stoc_number) * err_tolerance) - 1

