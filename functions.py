
def check_insertion (node, input):
    if len(input) <= len(node) or len(input) > len(node) + 2:
        print("wrong length")
        return False
    uniquecharacters = set(node)
    num_insertions = 0
    node_index = 0
    node += "  "
    for input_index in range(0,len(input)):
        if node[node_index] != input[input_index]:
            if not input[input_index] in uniquecharacters:
                num_insertions += 1
        else:
            node_index += 1
    return num_insertions


def check_deletion (node, input):
    num_deletions = 0
    input_index = 0
    if len(node) <= len(input) or len(node) > len(input) + 2:
        print("wrong length")
        return False
    if not set(input).issubset(set(node)):
        print("insertion")
        return False
    input += "  "
    for node_index in range(0,len(node)):
        if node[node_index] != input[input_index]:
            num_deletions += 1
        else:
            input_index += 1
    print(num_deletions)
    return num_deletions

