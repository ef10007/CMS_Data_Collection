# creates: band-alignment.png
from math import floor
import numpy as np
import matplotlib.pyplot as plt
import ase.db
from pprint import pprint

# Connect to database
db = ase.db.connect('c2db.db')

rows = db.select('Ba=1')

for row in rows:
    print(row.formula)
