from pymatgen import MPRester
from pprint import pprint
import os

JINNYAPI = os.environ['materials_project']
m = MPRester(JINNYAPI)

data = m.query({'piezo': {'$exists': True}}, ['material_id','pretty_formula', 'piezo'])
pprint(data)