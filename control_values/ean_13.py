from utils import use_first_digits


@use_first_digits(12)
def ean_13(digits):
    functions = [
        lambda x: x,
        lambda x: 3 * x
    ]
    sums = [0, 0]
    for i, digit in enumerate(digits):
        idx = i % 2
        sums[idx] += functions[idx](digit)
    last_digit = -sum(sums) % 10
    return locals()
