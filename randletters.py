
from random import randrange

cols = 41

def row():
    chars = [chr(ord('a') + randrange(26)) for i in range(cols)]
    return ' & '.join(chars) + r' \\' + '\n'
    
with open('giulia-tabular.tex', 'w') as f:
    f.write(r'\begin{tabular}' + '{{{}}}'.format('c' * cols) + '\n')
    for i in range(31):
        f.write(row())
    f.write(r'\end{tabular}')
