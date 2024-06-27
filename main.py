from src.services.prime_numbers import PrimeNumberCalculator
from src.services.arithmetic_sequence import ArithmeticSequence
from src.services.magic_quadrants import MagicQuadrants

DIMENSION = 9

def main(N):
    """
    Service that implements the calculation of magic squares formed by prime numbers.
    
    Attributes:
        N (int): The upper limit for calculating prime numbers.
    """
    prime_calculator = PrimeNumberCalculator(N)
    prime_numbers = prime_calculator.get_primes()
    print(prime_numbers)
    arithmetic_sequence = ArithmeticSequence(prime_numbers)
    arithmetic_sequence_per_dimension = arithmetic_sequence.find_sequence(n=DIMENSION)
    print(arithmetic_sequence_per_dimension)
    
    magic_quadrants = []
    for arithmetic_sequence_matrix in arithmetic_sequence_per_dimension:

        get_matrix = MagicQuadrants(arithmetic_sequence_matrix)
        
        is_magic_quadrant, matrix_results = get_matrix.get_magic_quadrant()

        if is_magic_quadrant:

            magic_quadrants.append({
                "name": f"Magic Quadrant {len(magic_quadrants) + 1}",
                "elements": matrix_results
            })
    
    return magic_quadrants

