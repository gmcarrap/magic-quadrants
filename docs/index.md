# Magic Quadrants

To calculate the magic squares first, all prime numbers in the interval between 0 and N are calculated, where N is the input value.

Then, the arithmetic sequences of length L=9 are calculated since we will work with matrices of DIMENSION = 9.

Finally, the matrices are formed following Green's and Tao's Theorem from the calculated arithmetic sequences. In addition, we will calculate if these matrices are magic squares and they will appear in the implemented API.

To test the execution follow the commands below:

## Commands

* `python api_server.py` - Raises the API server.
* `N` - Enter a value for N. For values of N greater than 2000 there are already magic squares.


## Project layout

        mkdocs.yml    # The configuration file.
        docs/
            api-implementation.md
            arithmetic_sequence.md
            index.md  
            magic-quadrants.md
            main.md
            prime-numbers.md
        src/
            services/
                arithmetic_sequence.py
                magic_quadrants.py
                prime_numbers.py
            tests/
        api_server.py
        main.py
    Readme.md
    requirements.txt
