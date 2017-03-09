from utils import use_first_digits


class LuhnLogger:
    """
    Хранение остатков от деления для отчёта
    """
    def __init__(self):
        self.values = []

    def calc_luhn_even(self, digit):
        result = (digit * 2) % 9
        self.values.append(result)
        return result

    def get_values(self):
        return reversed(self.values)


@use_first_digits(14)
def luhn(digits):
    keeper = LuhnLogger()
    functions = [
        lambda x: x,
        keeper.calc_luhn_even
    ]
    sums = [0, 0]
    even = len(digits) % 2
    for i, digit in enumerate(reversed(digits)):
        idx = i % 2
        sums[idx] += functions[idx](digit)
    last_digit = -sum(sums) % 10
    return locals()
