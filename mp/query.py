from pymatgen import MPRester
from pprint import pprint
import os
JINNYAPI = os.environ['materials_project']

import itertools
from zipfile import ZipFile

from pymatgen import Element, MPRester

# m = MPRester(JINNYAPI)


with MPRester(JINNYAPI) as m:

    data = m.query(criteria={"pretty_formula": "BaTiO3"}, properties=["pretty_formula", "material_id", "piezo", "spacegroup.crystal_system"])
    pprint(data)

