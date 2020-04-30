def instruction_menu():
    """
    this function holds the instruction menu

    :return: instruction menu
    """
    return (
        '''
----------------------------------------------------------
Welcome to Number Base converter!
This program will ask you for:
- The Number to convert
- The base you want to convert FROM
- The base you want to convert TO
- NOTE: Do not enter letters for any base
- In case of HEX, only use the HEX range.
----------------------------------------------------------
    ''')


def check_binary(check_number):
    """
    function that checks if the input consists of either 0 or 1.
    As the binary numbers can only be 0 or 1, so we need to check this
    before doing any calculations on it.

    :param check_number: the number entered by the user
    :return: True/False
    """
    check_list = [int(i) for i in (sorted(set(list(str(check_number)))))]

    print(f'\nchecking {check_number}')
    for number in check_list:
        if number not in [0, 1]:
            # print(f'invalid binary number')
            return False
    return True


def check_input(input_number):
    """
    function that checks if the input is from characters list or not.

    :param input_number: the number entered by the user
    :return True/False
    """

    char_list = '0123456789abcdef'
    for number in input_number:
        if number not in char_list:
            return False
    return True


def check_validity(input_number, input_base, output_base):
    if check_input(input_number) and input_base.isdigit() and output_base.isdigit():

        if int(input_base) == 2:
            if not input_number.isdigit():
                print(">>> ERROR: "
                      "Input is not in numbers. Binary Numbers are in 0s and 1s only.")
                return False

            elif not check_binary(input_number):
                print(">>> ERROR: "
                      "Invalid Binary Number. Must be in 0s or 1s only.")
                return False

        if int(input_base) == 1 or int(output_base) == 1:
            print(f'\nCan not convert to, or from Base 1')
            return False
        return True
    else:
        print(f">>>ERROR: "
              f"Invalid input... Try again")
        return False


def main_converter(input_number, input_base, output_base):
    """
    function that do convert numbers from one base to another

    :param input_number: the number entered by the user
    :param input_base: the base user wants to convert from
    :param output_base: the base user wants to convert to
    :return converted number
    """

    # this list holds the numbers to display at the end
    remainder_list = []

    # start value for base 10. As base 10 is our intermediate, in int_base_10, int means intermediate
    int_base_10 = 0

    # checking inputs
    if output_base == 2:
        return bin(input_number)[2:]

    # using the base 10 before the actual calculation as an intermediate
    elif input_base != 10:

        # reverse the string to start calculating from the least significant number,
        # the number as unit's place.
        reversed_input_number = input_number[::-1]

        # check if user typed in alphas outside HEX dictionary.
        dictionary_hex = {
            'a': 10,
            'b': 11,
            'c': 12,
            'd': 13,
            'e': 14,
            'f': 15
        }

        for i, number in enumerate(reversed_input_number):
            for key, value in dictionary_hex.items():
                if str(number).lower() == key:
                    number = value

            int_base_10 += (int(number) * (int(input_base) ** i))

    # if the number is already in Base 10, so we can start conversion
    elif input_base == 10:
        int_base_10 = int(input_number)

    # iterate through, until we hit 0. When we get 0, we'll have our number.
    while int_base_10 > 0:

        # find number to pass further down the loop, the number before the decimal point
        divided = int_base_10 // int(output_base)

        # find remainder to keep, the number after the decimal point
        remainder_list.append(str(int_base_10 % int(output_base)))

        # the new value to send to the next iteration
        int_base_10 = divided

    # if Hexadecimal output base, we should convert numbers above 9
    if int(output_base) == 16:
        hex_dictionary = {
            '10': 'a',
            '11': 'b',
            '12': 'c',
            '13': 'd',
            '14': 'e',
            '15': 'f'
        }

        # iterate through remainder_list and convert 9+ numbers to alphas.
        for i, each in enumerate(remainder_list):
            for key, value in hex_dictionary.items():
                if each == key:
                    remainder_list[i] = value

    return ''.join(remainder_list[::-1])


def main_menu():
    """
    function that interacts with the user and sends it to get converted.

    :return: interactions with user, input number and base, output base and the results.1
    """
    input_number = ''
    input_base = ''
    output_base = ''

    yes_or_no = 'y'

    while yes_or_no.lower() == 'y':
        valid_input = False
        while not valid_input:
            input_number = input('\nEnter number you want to convert: ')
            input_base = input('Enter the base you want to convert FROM: ')
            output_base = input('Enter the base you want to convert TO: ')

            valid_input = check_validity(input_number, input_base, output_base)

        print(
            f'\nTrying to convert '
            f'{input_number} '
            f'from Base {input_base} '
            f'to Base {output_base}:'
        )
        print(f'>> RESULT: '
              f'{main_converter(input_number, input_base, output_base)} ')

        print(f'\nWant to convert another number? Type y/n: ')
        yes_or_no = input('')

    print(f'Exiting converter....')


if __name__ == '__main__':
    # show the instruction menu:
    print(instruction_menu())

    # execute the main converter:
    main_menu()
