numers_to_decimals = { 'I' : 1,
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
    >>> convert_numerals(III)
    3
    >>> convert_numerals(VII)
    7
    >>> convert_numerals(CLXV)
    165
    >>> convert_numerals(MMMCMXCIX)
    3999
    """
    result = 0
    numer_list = [i for i in numeral]