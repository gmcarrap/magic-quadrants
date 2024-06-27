
DIMENSION = 9

class ArithmeticSequence:
    """
    Class to find arithmetic sequences within a list of integers.

    Attributes:
        list (list): List of integers where sequences will be searched.
        set_numbers (set): Set of unique numbers in the list.
        sequences (list): List to store found arithmetic sequences.

    Methods:
        find_sequence(n=9):
            Finds and returns all arithmetic sequences of length n within the list.
    """
    
    def __init__(self, list):
        """
        Initializes an instance of ArithmeticSequence.

        Args:
            lista (list): List of integers where sequences will be searched.
        """
        self.list = list
        self.set_numbers = set(list)
        self.sequences = []
        
    
    def find_sequence(self, n=DIMENSION):
        """
        Finds all arithmetic sequences of length n within the list.

        Args:
            n (int): Length of arithmetic sequences to search for (default: 9).

        Returns:
            list: List of found arithmetic sequences, each sequence is a list of integers.

        Notes:
            Uses a brute-force approach to search for arithmetic sequences in the list.
            Updates the `sequences` attribute with the found sequences.

        Example:
            >>> sequence = ArithmeticSequence([1, 2, 3, 5, 8, 13])
            >>> sequence.find_sequence(3)
            [[1, 2, 3], [2, 3, 5], [1, 3, 5]]
        """

        for first_number in range(len(self.list)):
            print(first_number)
            for second_number in range(first_number + 1, len(self.list)):
                
                difference = self.list[second_number] - self.list[first_number]
                
                possible_succession = [self.list[first_number], self.list[second_number]]

                for comparison_following_numbers in range(2, n):
                    
                    next_number = self.list[second_number] + difference
                    
                    if next_number in self.set_numbers:
                        
                        possible_succession.append(next_number)
                        
                        second_number = self.list.index(next_number) 
                         
                    else:
                        break

                if len(possible_succession) == n:
                    
                    self.sequences.append(possible_succession)
                    
        return self.sequences
    
