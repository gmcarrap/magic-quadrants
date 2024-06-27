# Magic Quadrants

To calculate the magic squares first, all prime numbers in the interval between 0 and N are calculated, where N is the input value.

Then, the arithmetic sequences of length L=9 are calculated since we will work with matrices of DIMENSION = 9.

Finally, the matrices are formed following Green's and Tao's Theorem from the calculated arithmetic sequences. In addition, we will calculate if these matrices are magic squares and they will appear in the implemented API.

## Index

- [Description](#description)
- [Instalación](#instalación)
- [Documentation](#documentation)
- [API Usage](#API_Usage)

## Description

The following service has been implemented to calculate the magic squares formed by prime numbers. 

A magic square of size N is a matrix formed by N squares. So that the sum of each row, column and diagonals is equal. The most famous magic square was named “Lo Shu” and has the form:

                                    4   9   2
                                    3   5   7
                                    8   1   6
                    
If we notice, the values of such a magic square contain an arithmetic succession, that is, the difference between the values is always equal.

Because, in order to calculate magic squares formed by prime numbers, we are going to look for those sets of prime numbers of dimension N that fulfill an arithmetic sequence. This is known as the Green and Tao theorem.

## Instalación

Step-by-step instructions on how to install the project. Includes any necessary prerequisites.

- Clone the repository

  `git clone https://github.com/gmcarrap/magic-quadrants.git`

- Enter the project directory
  `cd magic-quadrants`

- Installs the runtime environment
  `conda create -n magicquadrants python=3.8`

- Install the requirements
  `pip install -r requirements.txt`

## Documentation

- Execute the documentation
  `mkdocs serve`

- Enter the address 
  `http://127.0.0.1:8000/`

There you can find all the documentation of the implemented services. In Home there is an index of the documentation itself.

## API Usage

- Execute
  `python apy_server.py`

- Enter the address
  `http://127.0.0.1:5000/magic-quadrants`
    ### Enjoy square matrices with prime numbers!
- Enter a value of N (a value greater than 2000 is recommended, as it is the first magic square with prime numbers up to N)





