from pymatgen import MPRester
from pprint import pprint
import os
JINNYAPI = os.environ['materials_project']

from pymatgen import Element, MPRester

# m = MPRester(JINNYAPI)

""" Properties - can be extended list with .extend() """

basic = ['pretty_formula', 'unit_cell_formula', 'icsd_ids', 'energy', 'energy_per_atom', 'volume', 'density', 'nsites','elements', 'nelements', 'spacegroup', 'initial_structure', 'final_structure', 'structure', 'cif']

Thermodynamic = ['formation_energy_per_atom', 'e_above_hull']

Mechanical = ['elasticity', 'piezo', 'diel']


with MPRester(JINNYAPI) as m:

    data = m.query({"pretty_formula": "BaTiO3"}, properties=basic)
    pprint(data)

