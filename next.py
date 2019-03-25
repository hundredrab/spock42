from random import randint

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f += 6
    return True


def next_prime(number):
    """Return the next prime."""
    next_number = number + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number

pf = 'test_next/'

for i in range(100):
    a = randint(1, 1000000)
    if i<30: a = randint(1,100)
    if i==1: a = 1
    print(a, next_prime(a)-a)
    input_file = f'{pf}input/input{i}.txt'
    out_file = f'{pf}output/output{i}.txt'
    print(input_file)
    with open(input_file, 'w') as f:
        f.writelines([str(a)])
    with open(out_file, 'w') as f:
        f.writelines([str(next_prime(a)-a)])
