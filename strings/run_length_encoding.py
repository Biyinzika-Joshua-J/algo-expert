"""
    input: string
    output: return first non repeating character index
"""

def run_length_encoding(string):
    chars_hash = {}
    for letter in string:
        if letter not in chars_hash:
            chars_hash[letter] = 0
        chars_hash[letter] += 1
    for idx, letter in enumerate(string):
        if chars_hash[letter] == 1:
            return idx
    return -1



string = 'abcdcaf'
string2='aaabbcc'

print(run_length_encoding(string2))