from src.generate_prime import GeneratePrime

def test_correct_generation_primes():
    UPTO_N = 1000
    FULL_MATCH_STR = "full_match"
    SOME_MISMATCH_STR = "some_mismatch"
    primeObj = GeneratePrime()
    primeObj.yield_prime(UPTO_N)
    FULL_MATCH = primeObj.compare_against_known_result()
    assert FULL_MATCH