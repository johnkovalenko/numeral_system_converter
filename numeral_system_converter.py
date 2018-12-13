#!/bin/python3

__author__ = 'Ivan Kovalenko'


hex_dict = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F'}


def translate_from_hex(number):

    for _digit, _char in hex_dict.items():

        while _char in number:
            number = number.replace(_char, _digit)

    return number


def decimal_to_other(number, new_system):
    # Convert from decimal

    new_system = int(new_system)
    number = int(number)
    new_number = []

    while number > 0:
        _digit = number % new_system
        # Get next digit of a new number.

        new_number.insert(0, str(_digit))

        number //= new_system
        # Make number quotient.

    return ''.join(new_number)


def other_to_decimal(number, base_system):
    # Convert to decimal.
    new_number = 0

    if base_system == '16':
        number = translate_from_hex(number)

    for _index, _digit in enumerate(str(number)):
        # Convert by algorithm where:
        # XYZ in base numeral system =
        # sum(X*base^2 + Y*base^1 + Z*base^0) in 10 numeral system.

        multiplication_index = (len(number) - 1) - _index
        # Reverse indexes to make correct multiplications while
        # convertation.

        new_number += int(_digit) * int(base_system) ** multiplication_index

    return new_number


def convert_to_hex(number):
    number = list(number)

    for _index in range(len(number)-2, 0, -1):
        # Slice number by two digits.
        _slice = ''.join(number[_index:_index+2])

        if (_slice in hex_dict.keys()) and (_index % 2 != 0):
            # Check if matching with hex_dict and replace with value if True.
            number[_index:_index+2] = hex_dict[_slice]

    return ''.join(number)


def convert_systems(number, base_system, new_system):
    '''Convert given number from one numeral system to another, using Horner`s
    method.

    Script just divide a number, to be converted, by a base with a reminder.
    Reminder becomes a digit of a new base number.
    Do the same with a quotient from previous step, until reminder equals
    zero.
    Idea borrowed from the lector of Timofey Fedorovich Khiryanov,
    senior lecturer of MIPT.
    http://wikimipt.org/wiki/Хирьянов_Тимофей_Федорович
    '''

    # base_system, new_system = int(base_system), int(new_system)

    if number == 0:
        output = 0

    elif base_system == 10:
        output = decimal_to_other(number, new_system)

    elif new_system == 10:
        output = other_to_decimal(number, base_system)

    else:
        transient = other_to_decimal(number, base_system)
        # Firstly, convert to decimal, then to final number.

        output = decimal_to_other(transient, new_system)

    if new_system == '16':
        output = convert_to_hex(output)

    return output


if __name__ == '__main__':

    # number, base_system, new_system = input(
    #     'Please, base three args: \n'
    #     'number, its numeral system and a system of new number: \n'
    #     '>>> ').split()

    # print('\nThe new number in {}x numeral system is {}'.
    #       format(new_system,
    #              convert_systems(number, base_system, new_system)))

    # Testing the convertor script.
    # Use following table: Dec Bin Oct Hex.
    ex1 = {'0': '31', '2': '11111', '8': '37', '16': '1F'}

    predicates = [
    ]

    def test_by_predicates(array):
        pass

    print(test_by_predicates(ex1))
