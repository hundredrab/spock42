from collections import *
from random import randint, choice
from string import ascii_lowercase

pf = 'test_anna/'

for i in range(100):
    if i < 10:
        i = '0' + str(i)
    input_file = f'{pf}input/input{i}.txt'
    out_file = f'{pf}output/output{i}.txt'
    print(input_file)
    sa = "".join([choice(ascii_lowercase) for i in range(randint(1, 100))])
    sb = "".join([choice(ascii_lowercase) for i in range(randint(1, 100))])
    a = Counter(sa)
    b = Counter(sb)
    c = a - b
    d = b - a
    e = c + d
    print(sa, sb, len(list(e.elements())))
    with open(input_file, 'w') as f:
        f.writelines([sa, '\n',sb])
    with open(out_file, 'w') as f:
        f.writelines([str(len(list(e.elements())))+'\n'])
