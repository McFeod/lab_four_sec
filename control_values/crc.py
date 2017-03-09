import math

from utils import message_bits


def crc(message):
    polynomial = 0x13  # x**4 + x**1 + x**0
    n = int(math.log2(polynomial))
    mask = 2**n - 1
    it = iter(message_bits(message, n))
    bits = list(iter(message_bits(message, n)))  # для отчёта
    result = 0
    for _ in range(n + 1):
        result = (result << 1) + next(it)  # начальные биты
    steps = [result]
    for bit in it:
        result = (((result ^ polynomial) & mask) << 1) + bit  # деление с остатком
        steps.append(result)
    return locals()
