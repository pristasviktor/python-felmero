from src.math import *


def test_biggest_prime_divisor():
    assert biggest_prime_divisor(10) == 5
    assert biggest_prime_divisor(28) == 7
    assert biggest_prime_divisor(49) == 7
    assert biggest_prime_divisor(2) == 2
    assert biggest_prime_divisor(1) == 1
    assert biggest_prime_divisor(0) == 0
    assert biggest_prime_divisor(-15) == 5

def test_generate_primes_between():
    assert generate_primes_between(10, 20) == [11, 13, 17, 19]
    assert generate_primes_between(2, 10) == [2, 3, 5, 7]
    assert generate_primes_between(20, 30) == [23, 29]
    assert generate_primes_between(1, 5) == [2, 3, 5]
    assert generate_primes_between(0, 1) == []
    assert generate_primes_between(-10, 10) == [2, 3, 5, 7]
    assert generate_primes_between(10, 10) == []
