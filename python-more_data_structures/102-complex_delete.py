#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
print(complex_delete({'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}, 'C'))
