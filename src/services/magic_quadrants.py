from itertools import chain
import numpy as np

DIMENSION = 9

class MagicQuadrants:
    """
    The class calculates the magic matrix following the Green Tao Theorem. The theorem calculates the magic 
    squares of arithmetic sequences based on the magic square of “Lo Shu”.
    
    Attributes:
        arithmetic_sequence (list): List of prime numbers satisfying an arithmetic sequence of length N.
    """
    
    def __init__(self, elements):
        """
        From an input list it checks if it has the necessary values to form the matrix of the set dimension.

        Args:
            elements (list): List of numbers that fulfill an arithmetic sequence.

        Raises:
            ValueError: Return If the list contains exactly the number of elements equal to the dimension of the matrix.
        """
        if len(elements) != DIMENSION:
            raise ValueError("The list must contain exactly the number of elements equal to the dimension of the matrix")
        self.elements = elements

    def get_matrix(self):
        """
        Assuming the positions of the numbers of the “Lo Shu” base matrix, from an ascendingly ordered list 
        of numbers of dimension N, the positions where the numbers of the arithmetic sequence will form a square
        matrix can be established without using computational time.

        Returns:
            matrix: Magic quadrant formed by prime numbers.
        """
        
        matrix = [[0]*3 for _ in range(int(np.sqrt(DIMENSION)))]
        
        matrix[0][0], matrix[0][1], matrix[0][2] = self.elements[3], self.elements[8], self.elements[1]
        matrix[1][0], matrix[1][1], matrix[1][2] = self.elements[2], self.elements[4], self.elements[6]
        matrix[2][0], matrix[2][1], matrix[2][2] = self.elements[7], self.elements[0], self.elements[5]
        
        return matrix

    def get_magic_quadrant(self):
        """
        Check if the matrix formed from Green Tao's theorem of arithmetic sequences is a magic square.

        Returns:
            bool, list: returns whether the array is a magic square or not, plus the array if it is.
        """
        matrix_formed = self.get_matrix()

        reference_sum = sum(matrix_formed[0])
        
        for row in matrix_formed:
            
            if sum(row) != reference_sum:
                return False
        
        for column in range(int(np.sqrt(DIMENSION))):
            
            colum_sum = 0
            
            for row in range(int(np.sqrt(DIMENSION))):
                
                colum_sum += matrix_formed[row][column]
                
            if colum_sum != reference_sum:
                
                return False
        
        main_diagonal_sum = sum(matrix_formed[diagonal][diagonal] for diagonal in range(int(np.sqrt(DIMENSION))))
        
        if main_diagonal_sum != reference_sum:
            
            return False
        
        secondary_diagonal_sum = sum(matrix_formed[diagonal][2-diagonal] for diagonal in range(int(np.sqrt(DIMENSION))))
        
        if secondary_diagonal_sum != reference_sum:
            return False
        
        matrix = list(chain(*matrix_formed))
        return True, matrix


