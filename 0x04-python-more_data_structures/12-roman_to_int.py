#!/usr/bin/python3
def roman_to_int(roman_string):
    i = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    j = 0
    if not roman_string or type(roman_string) != str:
        return(0)
    for rom in range(len(roman_string)):
        if rom > 0 and i[roman_string[rom]] > i[roman_string[rom - 1]]:
            j += i[roman_string[rom]] - 2 * \
                    i[roman_string[rom - 1]]
        else:
            j += i[roman_string[rom]]
    return(j)
