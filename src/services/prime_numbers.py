from itertools import combinations

FIRST_PRIME_NUMBER = 2

class PrimeNumberCalculator:
    """
    A class to calculate prime numbers up to a specified maximum number using the Sieve of Eratosthenes.
    
    Attributes:
        max_number (int): The upper limit for calculating prime numbers.
        primes_numbers (list): A list to store the calculated prime numbers.
    """
    
    def __init__(self, max_number):
        """
        Initializes a PrimeNumberCalculator object with the given maximum number.
        
        Args:
            max_number (int): The maximum number up to which to calculate prime numbers.
        """
        
        self.max_number = max_number
        self.primes_numbers = []
        self._calculate_primes()

    def _calculate_primes(self):
        """
        Calculates all prime numbers up to the maximum number using the Sieve of 
        Eratosthenes algorithm.

        This method implements the Sieve of Eratosthenes algorithm to calculate all 
        prime numbers up to the maximum number specified in the instance of PrimeNumberCalculator.
            
        Returns:
            primes_numbers (list): A list of calculated prime numbers.
        """

        list_all_numbers = [True] * (self.max_number + 1)
        list_all_numbers[0] = list_all_numbers[1] = False
    
        for number in range(FIRST_PRIME_NUMBER, self.max_number + 1):
            if list_all_numbers[number]:
                for index_number_prime in range(number * number, self.max_number + 1, number):
                    list_all_numbers[index_number_prime] = False
                
                self.primes_numbers.append(number)
        
        prime_numbers = self.get_primes()
        
        return prime_numbers
    
    def get_primes(self):
        """
        Returns the list of calculated prime numbers.

        Returns:
            primes_numbers (list): A list of calculated prime numbers.
        """
        return self.primes_numbers
    

