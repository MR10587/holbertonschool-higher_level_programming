#!/usr/bin/python3
def roman_to_int(roman_string):
    # dictionary of characters as key and values
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
             'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}

    # add values to total
    i, total = 0, 0
    if type(roman_string) is str:
        while i < len(roman_string):
            if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman:
                total += roman[roman_string[i:i + 2]]
                i += 2
            else:
                total += roman[roman_string[i]]
                i += 1
        return total
    else:
        return 0
