from math import floor
import numpy as np
import matplotlib.pyplot as plt
from ase.db import connect
from pprint import pprint

# Connect to database
# db = connect('c2db.db', type='db')
# rows = db.select('C=2')

with connect('c2db.db') as db:
    print('Connected.') 
    print('There are {} rows found.'.format(len(list(enumerate(db.select('C=1'))))))

    for d in db.select('C=1'):
    
        print('formula', d.formula)
        print('id', d.id)
        print('numbers', d.numbers)
        print('cell', d.cell)

        print('atoms', db.get_atoms(d.id))

