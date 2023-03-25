numers_dict = { 'I' : 1,
                'V' : 5,
                'X' : 10,
                'L' : 50,
                'C' : 100,
                'D' : 500,
                'M' : 1000
                }

def check_valid(numeral):
    """
    Returns Boolean value corrresponding to if the Roman Numeral (numeral; passed in as a string) was written correctly.
    >>> check_valid('IV')
    True
    >>> check_valid('IX')
    True
    >>> check_valid('VX')
    False
    >>> check_valid('XL')
    True
    >>> check_valid('XC')
    True
    >>> check_valid('XD')
    False
    >>> check_valid('LC')
    False
    >>> check_valid('CD')
    True
    >>> check_valid('CM')
    True
    >>> check_valid('DM')
    False
    """
    numer_list = [i for i in numeral]
    
    def recurse(list_numerals):
        """
        helper recursive function for check_valid()
        """
        # base cases
        if len(list_numerals) <= 1:
            return True
        if numers_dict[list_numerals[0]] >= numers_dict[list_numerals[1]]:
            return recurse(list_numerals[2:])
        
        # other cases
        else:
            first = numers_dict[list_numerals[0]]
            second = numers_dict[list_numerals[1]]

            # case for any of the numerals that equate to 5 * n where n is any number
            if list_numerals[0] == 'V' or list_numerals[0] == 'L' or list_numerals[0] == 'D':
                return False
            
            return recurse(list_numerals[2:])

    return recurse(numer_list)


print(check_valid('IV'))
print(check_valid('IX'))
print(check_valid('VX'))
print(check_valid('XL'))



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
        helper recursive function for convert_numerals()
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
