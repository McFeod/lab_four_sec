def nonzero_count(byte):
    """
    Подсчёт числа ненулевых бит в байте/числе
    """
    result = 0
    while byte:
        byte ^= byte & (~byte + 1)
        result += 1
    return result


def as_bits(byte):
    return '{:08b}'.format(byte)


def odd_even(message, encoding='cp1251'):
    bytes_ = message.encode(encoding)
    rows = [{
        'char': char,
        'code': as_bits(byte),
        'even': nonzero_count(byte) % 2
    } for byte, char in zip(bytes_, message)]
    return locals()
