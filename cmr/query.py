# creates: band-alignment.png
from math import floor
import numpy as np
import matplotlib.pyplot as plt
import ase.db
from pprint import pprint

# Connect to database
db = ase.db.connect('cubic_perovskites.db')

rows = db.select('BaTiO3')

# <AtomsRow: formula=BaTiO3, keys=project,A_ion,anion,combination,CB_ind,gllbsc_ind_gap,heat_of_formation_all,CB_dir,gllbsc_dir_gap,standard_energy,B_ion,VB_dir,VB_ind>

for row in rows:
    print('-----------------------------------')
    print('formula: ', row.formula)
    print('project: ', row.project)
    print('A_ion: ', row.A_ion)
    print('anion: ', row.anion)
    print('combination: ', row.combination)
    print('CB_ind: ', row.CB_ind)
    print('gllbsc_ind_gap: ', row.gllbsc_ind_gap)
    print('heat_of_formation_all: ', row.heat_of_formation_all)
    print('CB_dir: ', row.CB_dir)
    print('gllbsc_dir_gap: ', row.gllbsc_dir_gap)
    print('standard_energy: ', row.standard_energy)
    print('B_ion: ', row.B_ion)
    print('VB_dir: ', row.VB_dir)
    print('VB_ind: ', row.VB_ind)

    


