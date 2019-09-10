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
    
    d = db.select('C=2')

    print(len(list(enumerate(db.select('')))))
        # print('id', d.id)
        # print('numbers', d.numbers)
        # print('cell', d.cell)

    #     atoms = db.get_atoms(d.id)
    #     print(atoms)
#         images.append(atoms)
# pprint(images)
