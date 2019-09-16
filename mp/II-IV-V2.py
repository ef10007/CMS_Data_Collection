from pymatgen import MPRester
from pprint import pprint
import os
JINNYAPI = os.environ['materials_project']

import csv
import itertools
from zipfile import ZipFile

from pymatgen import Element, MPRester

# m = MPRester(JINNYAPI)

def get_alkaline():
    return [el.symbol for el in Element if el.is_alkaline]

def get_crystallogens():
    return [el.symbol for el in Element if el.group == 14]

def get_pnictogens():
    return [el.symbol for el in Element if el.group == 15]

def get_double_pnictogens():
    nlst = get_pnictogens()
    for i in range(len(nlst)):
        nlst[i] = nlst[i] + '2'
    return nlst

def get_semiconductors_chemsys():
    
    g2 = get_alkaline()
    g4 = get_crystallogens()
    g5 = get_pnictogens()

    return sorted(["{}-{}-{}".format(*sorted(pair))
                    for pair in itertools.product(g2, g4, g5)])

def get_list():
    with MPRester(JINNYAPI) as m:
        data = m.query({'chemsys': {'$in': get_semiconductors_chemsys()} }, ['material_id', 'pretty_formula'])

        for i in range(len(data)):
            formula = data[i]['pretty_formula']

            # if any("abc" in s for s in some_list):
            for j in get_double_pnictogens():
                if j not in formula:
                    continue

                print(formula)

        # return data

get_list()
# print(lst)


# with MPRester(JINNYAPI) as m:
#     data = m.query(criteria={"formula_reduced_abc": "C Mg N2"}, properties=["material_id", "spacegroup.symbol"])
#     pprint(data)


# with ZipFile('zintl_cifs.zip', 'w') as f:
#     for d in docs:
#         f.writestr('{}_{}.cif'.format(d['pretty_formula'], d['material_id']),
#                    d['cif'])
