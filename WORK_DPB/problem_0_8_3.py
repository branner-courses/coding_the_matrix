# Problem 0.8.3

def tuple_sum(A, B):
    return [(a[0] + b[0], a[1] + b[1]) for a, b in zip(A, B)]
