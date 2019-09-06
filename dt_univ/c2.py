from math import floor
import numpy as np
import matplotlib.pyplot as plt
from ase.db import connect
from pprint import pprint

# Connect to database
# db = connect('c2db.db', type='db')

# rows = db.select('Ru=2')

with connect('c2db.db') as db:
    print('Connected.')  

    for i, d in enumerate(db.select('C=1')):
        # print('id', d.id)
        # print('numbers', d.numbers)
        # print('cell', d.cell)

    #     atoms = db.get_atoms(d.id)
    #     print(atoms)
#         images.append(atoms)
# pprint(images)
