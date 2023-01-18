def fibonacci_function(to_step):
    f1 = f2 = 1
    count = 2
    while count < to_step:
        fsum = f1 + f2
        f1 = f2
        f2 = fsum
        count += 1
    return f2



