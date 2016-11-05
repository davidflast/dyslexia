vowels = set(["a","e","i","o","u"])


def check_vowel_insertion(node, input):
    node_consonants = []
    input_consonants = []
    for char in node:
        if char not in vowels:
            node_consonants.append(char)
    for char in input:
        if char not in vowels:
            input_consonants.append(char)
    return node_consonants == input_consonants


print(check_vowel_insertion("hll", "hello"))