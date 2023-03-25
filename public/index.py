#!python3

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
    >>> check_valid('IL')
    False
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
    
    # check individual letters to see if they are keys
    for i in numer_list:
        if i not in numers_dict:
            return False
    
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
            
            # other cases
            if (first * 10) + 1 < second:
                return False
            return recurse(list_numerals[2:])

    return recurse(numer_list)


def parse_type():
    """
    Takes user input, and checks to see if it is a valid type. 
    If it is a valid input, return the input in the correct type.
    If it is not a valid input, returns false.

    **Special: if input is a Roman Numeral, check to see if it is a valid Roman Numeral.
    
    For the doctests, the parameters passed in are just examples of inputs the user could choose.
    >>> parse_type('IV')
    'IV'
    >>> parse_type('1234')
    1234
    >>> parse_type('12a1')
    False
    >>> parse_type('dClXv')
    'DCLXV'
    >>> parse_type('IL')
    False
    >>> parse_type('a')
    """
    while True:
        u_input = input('Enter: ')

        if u_input.isnumeric():
            return u_input
        elif u_input == 'q':
            break
        elif u_input.isalpha() and u_input.isupper():
            if check_valid(u_input):
                return u_input
            pass
        elif u_input.isalpha() and not u_input.isupper():
            result = ''
            for i in u_input:
                result += i.upper()
            if check_valid(result):
                return result
            pass
        print(f"\nInvalid input type, please try again.\n")


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


def convert_numbers(number):
    """
    Returns a given number (type == int) to a Roman Numeral.
    >>> convert_numbers(3)
    III
    >>> convert_numbers(7)
    VII
    >>> convert_numbers(165)
    CLXV
    >>> convert_numbers(3999)
    MMMCMXCIX
    """
    number = int(number)
    if number >= 1000:
        return 'M' + str(convert_numbers(number-1000))
    if number >= 900:
        return 'CM' + str(convert_numbers(number-900))
    if number >= 500:
        temp = number // 100
        num_of_Cs = temp-5
        return 'D' + 'C'*num_of_Cs + str(convert_numbers(number-(temp*100)))
    if number >= 400:
        return 'C' + 'D' + str(convert_numbers(number-400))
    if number >= 100:
        num_of_Cs = number // 100
        return 'C'*num_of_Cs + str(convert_numbers(number-(num_of_Cs*100)))
    if number >= 90:
        return 'XC' + str(convert_numbers(number-90))
    if number >= 50:
        temp = number // 10
        num_of_Xs = temp-5
        return 'L' + 'X'*num_of_Xs + str(convert_numbers(number-(temp*10)))
    if number >= 40:
        return 'X' + 'L' + str(convert_numbers(number-40))
    if number >= 10:
        num_of_Xs = number // 10
        return 'X'*num_of_Xs + str(convert_numbers(number-(num_of_Xs*10)))
    if number == 9:
        return 'IX'
    if number >= 5:
        temp = number // 1
        num_of_Is = temp-5
        return 'V' + 'I'*num_of_Is
    if number == 4:
        return 'IV'
    if number >= 1:
        return 'I'*number
    

def main():
    print("\nWelcome to Roman Numeral Converter!\n- Input either a Number or a Roman Numeral to switch it's type.\n- Enter 'q' to quit.")

    while True:
        result = None
        user_input = parse_type()

        if user_input == None:
            break
        if user_input.isnumeric():
            result = convert_numbers(user_input)
        if user_input.isalpha():
            result = convert_numerals(user_input)
        
        print(f"Result: {result}\n")
        
    print(f'Come back Soon!\n')

main()