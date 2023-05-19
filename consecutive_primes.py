import math


def is_prime(x: int) -> bool:
    """Return True if x is prime, False otherwise."""
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    N_NUMBERS = 8
    for y in range(0, 1_000):
        s = ''.join([str(x) for x in range(y, y + N_NUMBERS)])
        x = int(s)
        if is_prime(x):
            print(x)
