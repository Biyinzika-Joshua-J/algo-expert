"""
    input: non empty string with lower case chars from the english alphabet.. and an integer 
    value that will be used to shift every letter in the input string 
"""
import string


def caesar_cipher_modulo(input_string, shift_num):
    start_index = ord('a')
    end_index = ord('z')
    result = []
    for letter in input_string:
        new_letter_index = ord(letter) + shift_num
        if new_letter_index <= end_index:
            result.append(chr(new_letter_index))
        else:
            index = start_index + new_letter_index%end_index
            while index < end_index:
                index=start_index + new_letter_index%end_index
            result.append(chr((start_index + new_letter_index%end_index)-1))
    return ''.join(result)

def caesar_cipher(input_string, shift_num):
    alphabet = []
    alphabet_end_index = 26
    for letter_code in range(ord('a'), ord('z') + 1):
        alphabet.append(chr(letter_code))
    input_string_indices = [alphabet.index(char) for char in input_string]
    alphabet_indices = [index for index in range(0, len(alphabet))]

    result = []
    for index in input_string_indices:
        shifted_index = index + shift_num
        while shifted_index >= alphabet_end_index:
            shifted_index_difference = shifted_index - 26
            shifted_index = shifted_index_difference
        result.append(alphabet[shifted_index])
    return ''.join(result)

    

    
"""
    alpabet 
    -------
    a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
"""
input = 'xyz' # zab
shift = 54

# tests the understanding of the modulo operator
print(caesar_cipher(input, shift))
print(caesar_cipher_modulo(input, shift))