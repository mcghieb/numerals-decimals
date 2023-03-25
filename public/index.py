numers_dict = { 'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
                }


def convert_numerals(numeral):
    """
    Returns a given Roman Numeral (numeral; passed in as a string) to a Decimal Number.
    >>> convert_numerals('III')
    3
    >>> convert_numerals('VII')
    7
    >>> convert_numerals('CLXV')
    165
    >>> convert_numerals('MMMCMXCIX')
    3999
    """
    numer_list = [i for i in numeral]

    def recurse(list_numerals):
        """
        helper recursive function for convert_numerals
        """
        # base cases
        if len(list_numerals) == 1:
            return numers_dict[list_numerals[0]]
        if len(list_numerals) < 1:
            return 0
        
        # normal descending numeral case
        if numers_dict[list_numerals[0]] >= numers_dict[list_numerals[1]]:
            x = numers_dict[list_numerals[0]]
            return x + recurse(list_numerals[1:])
        
        # other cases
        elif numers_dict[list_numerals[0]] <= numers_dict[list_numerals[1]]:
            x = numers_dict[list_numerals[1]] - numers_dict[list_numerals[0]]
            return x + recurse(list_numerals[2:])
    
    return recurse(numer_list)

# working test cases
# print(convert_numerals('I'))
# print(convert_numerals('CLXV'))

# broken test cases
print(convert_numerals('MMMCMXCIX'))