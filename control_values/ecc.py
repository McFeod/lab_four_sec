import math
from random import choice

from control_values.odd_even_bit import nonzero_count
from utils import message_bits


class BitMatrix:
    """
    Создание матрицы для ECC. Строки бит в матрице представлены числами
    """
    def __init__(self, length):
        self.length = length
        self.rows = [self.make_row(1 << power) for power in range(math.ceil(math.log2(length)))]

    def make_row(self, power):
        addition = (1 << power) - 1
        result = 0
        for i in range(0, self.length + 1, power):
            result <<= power
            if i % (power << 1):
                result += addition
        return result

    def __str__(self):
        return ' \\\\ \n '.join(format_binary(row, self.length) for row in self.rows)

    def __mul__(self, vector):
        """
        Умножение транспонированной матрицы на вектор по модулю 2
        """
        return list(map(lambda x: nonzero_count(x & vector) % 2, self.rows))


def format_binary(num, zero_count):
    return ('{:0%db}' % zero_count).format(num)


def insert_control_bits(message, control_bits):
    """
    Вставка контрольных бит на места с индексами 2**n
    :param message: исходное сообщение
    :param control_bits: контольные биты
    :return: измененное сообщение
    """
    it = iter(message)
    result = 0
    for i, bit in enumerate(control_bits):
        result = (result << 1) + bit
        for _ in range((1 << i) - 1):
            result = (result << 1) + next(it)
    return result


def ecc_control_sum(message, r=4):
    """
    Полдсчёт контрольной суммы ECC
    """
    source = list(message_bits(message))[:(1 << r) - r - 1]
    xr = insert_control_bits(source, [0]*r)
    matrix = BitMatrix((1 << r) - 1)
    control_sum = matrix * xr
    return locals()


def bits_to_int(bits):
    return sum((bit << i) for i, bit in enumerate(bits))


def make_error(message, r, errors=1):
    sum_steps = ecc_control_sum(message, r)
    bits = sum_steps['source'] + sum_steps['control_sum']
    correct = [i for i, _ in enumerate(bits)]
    for _ in range(errors):
        idx = choice(correct)
        correct.remove(idx)
        bits[idx] = int(not bits[idx])
    return bits


def restore_message(message, error_count, r=4):
    """
    Попытка восстановить искажённое сообщение
    """
    bits = make_error(message, r, error_count)
    source = bits[:-r]
    control_bits = bits[-r:]
    matrix = BitMatrix(len(bits))
    xr = insert_control_bits(source, control_bits)
    pb = sum(bits) & 1
    syndromes = matrix * xr
    error_in = bits_to_int(syndromes)
    return locals()
