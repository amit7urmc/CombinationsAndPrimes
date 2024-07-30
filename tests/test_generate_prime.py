import os
from src.generate_prime import GeneratePrime

def test_correct_generation_primes():
    UPTO_N = 1000
    FULL_MATCH_STR = "full_match"
    SOME_MISMATCH_STR = "some_mismatch"
    CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
    primeObj = GeneratePrime(f"{CURRENT_DIR}/primeListGenerated.txt")
    primeObj.yield_prime(UPTO_N)
    FULL_MATCH = primeObj.compare_against_known_result(f"{CURRENT_DIR}/PrimeNumbersTop1000.txt")
    assert FULL_MATCH