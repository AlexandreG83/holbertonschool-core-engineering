def pow(a, b):
    """Returns a to the power of b."""
    if b < 0:
        a = 1 / a
        b = -b
    result = 1
    for _ in range(b):
        result *= a
    return result
