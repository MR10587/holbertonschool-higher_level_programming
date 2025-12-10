#!/usr/bin/python3
def roman_to_int(roman_string):
    # dictionary of character as key and values
    roman_num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    # add values to total
    character, total = 0, 0
    if type(roman_string) == str:
        while character < len(roman_string):
            if character + 1 < len(roman_string) and roman_string[character:character + 2] in roman_num:
                total += roman_num[roman_string[character:character + 2]]
                character +=2
            else:
                total += roman_num[roman_string[character]]
                character +=1
        return total
    else:
        return 0
