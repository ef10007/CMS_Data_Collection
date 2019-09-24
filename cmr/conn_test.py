# creates: band-alignment.png
from math import floor, ceil
import re
import numpy as np
import matplotlib.pyplot as plt
import ase.db
from pprint import pprint

# Connect to database
db = ase.db.connect('c2dm.db')

# Select the rows that have G0W0 results
rows = db.select('xc=LDA,ind_gap_g0w0>0')

data = []
for row in rows:
    name = row.name
    print('name :', name)
    
    # Use regular expressions to get the atomic species from the name
    m = re.search('([A-Z][a-z]?)([A-Z][a-z]?)2', name)
    M = m.group(1)
    X = m.group(2)

    print('M:', M, 'X:', X)
