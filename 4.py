def get_z(tup):
    result = []
    for word in tup:
        if word[0] == 'z':
            result.append(word)
    result_tup = tuple(result)
    return result_tup
print(get_z( ("zebra", "apple", "zero", "banana", "zoo")))
