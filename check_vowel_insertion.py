vowels = {"a", "e", "i", "o", "u"}


def check_vowel_insertion(node, data):
    node_consonants = [char for char in node if char not in vowels]
    input_consonants = [char for char in data if char not in vowels]
    return node_consonants == input_consonants
