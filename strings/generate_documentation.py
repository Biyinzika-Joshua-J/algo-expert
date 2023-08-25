"""
    input: string
    output: return first non repeating character index
"""
"""
    determine if with the available chars, the document string can be created 
    
"""

def generateDocument(characters, document):
    characeters_hash = generateMap(characters)
    document_hash = generateMap(document)
    return canGenerateDoc(characeters_hash, document_hash, document)

def canGenerateDoc(characters, document, document_str):
    for char in document_str:
        if char not in characters:
            return False
        if characters[char] < document[char]:
            return False
    return True

def generateMap(string):
    hash = {}
    for letter in string:
        if letter not in hash:
            hash[letter] = 0
        hash[letter] += 1
    return hash


characters = "Bste!hetsi ogEAxpelrt x " # true
document="AlgoExpert is the Best"

print(generateDocument(characters, document))