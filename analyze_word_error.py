from generate_arrays import generate_arrays
from function_error import is_function_error
from functions import lcs
from is_phonetic import is_phonetic
from generate_arrays import generate_arrays
from check_vowel_insertion import check_vowel_insertion

# returns an array of booleans
# Index
# 0: phonetic
# 1: function words
# 2: reversal
# 3: transposition
# 4: insertion (int)
# 5: deletion (int)
# 6: vowel_insertion


def word_error(autocorrect, mistake):
    output = dict(phonetic=False,
                  function_word=False,
                  reversal=False,
                  transposition=False,
                  insertion=False,
                  deletion = False,
                  vowel_insertion=False)
    if is_phonetic(autocorrect, mistake):
        output["phonetic"] = True
    output["function_word"] = is_function_error(autocorrect)
    if check_vowel_insertion(autocorrect, mistake):
        output["vowel_insertion"] = True
        return output
    branches_from_auto = generate_arrays(autocorrect)
    num_rows = len(branches_from_auto)
    num_cols = len(branches_from_auto[0])
    for col in range(num_cols):
        for row in range(num_rows):
            current = branches_from_auto[row][col]
            output["reversal"] = row != 0
            output["transposition"] = col != 0
            if current == mistake:
                return output
            least_common_string = len(lcs(mistake, current))
            if len(mistake) > len(current):
                if len(mistake) - least_common_string == 1:
                    output["insertion"] = True
                    return output
            if len(mistake) < len(current):
                if len(current) - least_common_string == 1:
                    output["deletion"] = True
                    return output
    output["reversal"] = False
    output["transposition"] = False
    output["insertion"] = False
    output["deletion"] = False
    output['vowel_insertion'] = False
    return output
print(word_error("hello", "helloo"))
