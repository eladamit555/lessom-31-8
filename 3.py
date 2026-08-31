def get_positive(tup):
    reult = []
    for num in tup:
        if num > 0:
            reult.append(num)
    reult_tuple = tuple(reult)
    return reult_tuple
print(get_positive( (-5, 8, -2, 10, 0, 3) ) )