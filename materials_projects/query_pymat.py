import json
import os
from pprint import pprint
from pymatgen import MPRester

JINNYAPI = os.environ['materials_project']

m = MPRester(JINNYAPI)

data = m.query(criteria={"elements": {"$in": ["K"]}}, properties=["pretty_formula", "piezo"])

for datum in data:
    if datum['piezo']!= None:
        print(datum['pretty_formula'])



