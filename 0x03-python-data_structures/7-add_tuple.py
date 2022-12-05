def add_tuple(tuple_a=(), tuple_b=()):
    while (len(tuple_a) < 2):
        tuple_a += (0,)
    while (len(tuple_b) < 2):
        tuple_b += (0,)

    sum1 = tuple_a[0] + tuple_b[0]
    sum2 = tuple_a[1] + tuple_b[1]

    return (sum1, sum2)
