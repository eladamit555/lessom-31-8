def sum_tups():

    tup1 = (10, 20, 30, 40)
    tup2 = (1,  2,  3,  4)
    result = []
    for i in range(len(tup1)):
        result.append(tup1[i] + tup2[i])
    result = tuple(result)
    return result
print(sum_tups())
