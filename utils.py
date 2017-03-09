def use1251(func):
    def wrapper(string, *args, **kwargs):
        return func(string.encode('cp1251'), *args, **kwargs)
    return wrapper


@use1251
def to_decimals(string):
    """
    Разбиение строки на десятичные цифры
    """
    for byte in string:
        for x in (100, 10, 1):
            yield byte // x
            byte %= x


def use_first_digits(n):
    """
    Отбрасывание лишних цифр
    """
    def decorator(func):
        def wrapper(message, *args, **kwargs):
            return func(list(to_decimals(message))[:n], *args, **kwargs)
        return wrapper
    return decorator


def bits(byte):
    """
    Итерация по битам одного байта
    """
    result = []
    for _ in range(8):
        result.append(byte & 1)
        byte >>= 1
    return reversed(result)


@use1251
def message_bits(message, extra_bits=0):
    """
    Итерация по битам строки
    :param message: строка
    :param extra_bits: число дописанных в конец нулевых бит
    """
    for byte in message:
        for bit in bits(byte):
            yield bit
    for _ in range(extra_bits):
        yield 0
