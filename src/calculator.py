def validate_numbers(*args):
    if not all(isinstance(i, (int, float)) for i in args):
        raise ValueError("All inputs must be numbers.")


def fun1(x, y):
    """Adds two numbers."""
    validate_numbers(x, y)
    return x + y


def fun2(x, y):
    """Subtracts y from x."""
    validate_numbers(x, y)
    return x - y


def fun3(x, y):
    """Multiplies two numbers."""
    validate_numbers(x, y)
    return x * y


def fun4(x, y, z):
    """Adds three numbers."""
    validate_numbers(x, y, z)
    return x + y + z
