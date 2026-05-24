def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int | float , b: int | float) -> float:
    if b == 0:
        raise ValueError('Делить на ноль нельзя')
    return a / b