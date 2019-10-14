
from pymatgen import Element, MPRester
from pprint import pprint
import os
JINNYAPI = os.environ['materials_project']

import itertools
from zipfile import ZipFile

# m = MPRester(JINNYAPI)

def get_alkaline():
    return [el.symbol for el in Element if el.is_alkaline or el.group == 12]

def get_crystallogens():
    return [el.symbol for el in Element if el.group == 14 or el.group == 4]

def get_pnictogens():
    return [el.symbol for el in Element if el.group == 15]

def get_double_pnictogens():
    nlst = get_pnictogens()
    for i in range(len(nlst)):
        nlst[i] = nlst[i] + '2'
    return nlst

def get_query_chemsys():
    g2 = get_alkaline()
    g4 = get_crystallogens()
    g5 = get_pnictogens()
    return sorted(["{}-{}-{}".format(*sorted(pair))
                    for pair in itertools.product(g2, g4, g5)])

def get_result(query, properties=['material_id', 'pretty_formula', 'cif']):
    with MPRester(JINNYAPI) as m:

        data = m.query({'chemsys': {'$in': query} }, properties)

        for d in itertools.chain(data):
            docs = {}
            mid = d['material_id']
            formula = d['pretty_formula']
            cif = d['cif']

            numbers = sum(letter.isdigit() for letter in formula)

            if numbers > 1 or '(' in formula:
                continue

            for j in get_double_pnictogens():
                if j not in formula:
                    continue

                docs['material_id'] = mid
                docs['pretty_formula'] = formula
                docs['cif'] = cif

                yield docs

def post_process_245(docs):
    for d in docs:
        if d['pretty_formula'][:2] not in get_alkaline():
            continue
        yield d

def post_process_425(docs):
    for d in docs:
        if d['pretty_formula'][:2] not in get_crystallogens():
            continue
        yield d

def write_cif(docs, filename):
    with ZipFile(filename, 'w') as f:
        for d in docs:
            f.writestr('{}_{}.cif'.format(d['pretty_formula'], d['material_id']), d['cif'])
        
    print('The cif files {} have been saved.'.format(filename))

docs = get_result(get_query_chemsys(), ['material_id', 'pretty_formula', 'cif'])
# compnd245 = post_process_245(docs)
compnd425 = post_process_425(docs)

# pprint([c for c in compnd425])
# write_cif(compnd245, 'II_IV_V2.zip')
write_cif(compnd425, 'IV_II_V2.zip')

