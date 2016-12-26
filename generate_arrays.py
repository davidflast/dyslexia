from itertools import combinations_with_replacement
from itertools import permutations
from itertools import product


reversal_letters = {'b', 'd', 'p', 'q', 'm', 'w'}
reversal_map = dict(b="d", d="b", p="q", q="p", m="w", w="m")


def generate_arrays(autocorrect):
    num_revs = len(list(x for x in autocorrect if x in reversal_letters))
    perms = product([True, False], repeat = num_revs)
    list_reversal = list()
    for p in perms:
        perm_string = ""
        auto_position = 0
        tf_position = 0;
        for c in autocorrect:
            if c in reversal_letters:
                if not p[tf_position]:
                    perm_string += reversal_map[c]
                    tf_position += 1
                else:
                    perm_string += c
                    tf_position += 1
            else:
                perm_string += c
        list_reversal.append(perm_string)
    final_list = list()
    rev_position = 0;
    for rev in list_reversal:
        final_list.append(["".join(x) for x in permutations(rev,r=len(rev))])
        rev_position += 1
    return final_list

