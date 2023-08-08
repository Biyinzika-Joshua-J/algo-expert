def knuth_morris_pratt(string, sub_string):
    pattern = build_pattern(sub_string)
    return does_match(string, sub_string, pattern)

def build_pattern(sub_string):
    pattern = [-1 for i in sub_string]
    j=0
    i=1
    while i < len(sub_string):
        if sub_string[i] == sub_string[j]: # got a prefix ending at j that is also a suffix ending at i
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1
    return pattern
        


def does_match(string, sub_string, pattern):
    i = 0
    j = 0
    while i + len(sub_string) -j <= len(string):
        if string[i] == sub_string[j]:
            if j == len(sub_string)-1:
                return True
            i+=1
            j+=1
        elif j > 0:
            j = pattern[j-1]+1
        else:
            i+=1
    return False

res = knuth_morris_pratt('aefaefaefaedaefaedaefaefa', 'aefaedaefaefa')
print(res)
print(knuth_morris_pratt('Biyinzika', 'inzi'))