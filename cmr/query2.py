# creates: band-alignment.png
from math import floor, ceil
import re
import numpy as np
import matplotlib.pyplot as plt
import ase.db
from pprint import pprint

# Connect to database
db = ase.db.connect('c2dm.db')

rows = db.select('')

for row in rows:
    print(row)
