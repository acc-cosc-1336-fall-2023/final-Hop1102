#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_most_likely_ancestor_consensus(dna_string1, dna_string2):
    positions = []
    start = 0

    while start < len(dna_string1):
        position = dna_string1.find(dna_string2, start)
        if position == -1:
            break
        positions.append(position + 1) 
        start = position + 1

    return tuple(positions) 

def validate_dna_string(dna_string):
    return len(dna_string) > 8 and len(dna_string) <= 17

def validate_dna_substring(dna_substring):
    return len(dna_substring) == 4