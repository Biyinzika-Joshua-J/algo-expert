"""
    data are stored as a single data value rather than the original count
    
"""

def run_length_encoding(string):
    encoding = []
    count = 1
    char = string[0]
    for idx, letter in enumerate(string):
        if idx != 0:
            if letter == char:
                count += 1
            else:
                if count > 9:
                    while count > 9:
                        value = f'{9}{char}'
                        encoding.append(value)
                        count = int(count % 9)

                    value = f'{count}{char}'
                    encoding.append(value)
                else:
                    value = f'{count}{char}'
                    encoding.append(value)
                count = 1
                char = letter
    if count > 9:
        while count > 9:
            value = f'{9}{char}'
            encoding.append(value)
            count = int(count % 9)

        value = f'{count}{char}'
        encoding.append(value)
    else:
        value = f'{count}{char}'
        encoding.append(value)
    count = 1
    char = letter
    return ''.join(encoding)


string = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAABBCCCCDD'
print(run_length_encoding(string))