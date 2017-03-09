from utils import use_first_digits


@use_first_digits(4)
def railway(digits):
    factors = range(1, 5)
    shift = 0
    last_digit = 10
    history = []
    while last_digit == 10:
        next_sum = sum(map(lambda x: x[0] * (x[1] + shift), zip(digits, factors)))
        history.append(next_sum)
        last_digit = next_sum % 11
        shift += 2
    return locals()
