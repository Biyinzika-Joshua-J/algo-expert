# a subsequnec is a sequence that can be drived from another sequence by deleting some or no elements without # changing the order of the remaining elements
def validateOptimized(array, sub_sequence):
    sub_sequence_pointer = 0
    for value in array:
        if value == sub_sequence[sub_sequence_pointer]:
            sub_sequence_pointer += 1
            if sub_sequence_pointer == len(sub_sequence):
                return True
    return False



def validate(array, sub_sequence):
    sub_sequence_idxs = [0 for _ in range(len(sub_sequence))]
    array_hash = {}
    for idx, value in enumerate(array):
        if value not in array_hash:
            
            array_hash[value] = idx
           
    for i in range(len(sub_sequence_idxs)):
        try:
            sub_sequence_idxs[i] = array_hash[sub_sequence[i]]
        except KeyError:
           return False
    
    sorted = [i for i in sub_sequence_idxs]
    sorted.sort()
    if sorted == sub_sequence_idxs:
        return True
    return False





print(validateOptimized([5,1,22,25,6,-1,8,10], [1,6,-1,10]))
