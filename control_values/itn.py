from utils import use_first_digits


@use_first_digits(9)
def itn(digits):
    # constants = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    constants = [2, 4, 10, 3, 5, 9, 4, 6, 8]
    both = list(zip(constants, digits))
    last_digit = (sum(map(lambda x: x[0] * x[1], both)) % 11) % 10
    return locals()
