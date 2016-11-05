from generate_arrays import generate_arrays
from function_error import is_function_error
from functions import check_deletion
from functions import check_insertion
from is_phonetic import is_phonetic

# returns an array of booleans
# Index
# 0: phonetic
# 1: function words
# 2: reversal
# 3: transposition
# 4: insertion (int)
# 5: deletion (int)
# 6: vowel_insertion


def word_error(autocorrect, input):
    output = dict(phonetic=False,
                  function_word=False,
                  reversal=False,
                  transposition=False,
                  insertion=0,
                  deletion=0,
                  vowel_insertion=False)
    if is_phonetic(autocorrect, input):
        output["phonetic"] = True
        return output
    output["function_word"] = is_function_error(autocorrect)
    test_array = generate_arrays(autocorrect)
    num_rows = len(test_array)
    num_cols = len(test_array)
    for row in range(num_rows):
        for col in range(num_cols):
            current = test_array[row][col]
            output["reversal"] = row != 0
            output["transposition"] = col != 0
            if current == input:
                return output
            deletions = check_deletion(current, input)
            insertions = check_insertion(current, input)
            if 3 > deletions > 0:
                output["deletion"] = deletions
                return output
            if 3 > insertions > 0:
                output["insertion"] = insertions
                return output
    output["reversal"] = False
    output["transposition"] = False
    output["insertion"] = 0
    output["deletion"] = 0
    output['vowel_insertion'] = False
    return output