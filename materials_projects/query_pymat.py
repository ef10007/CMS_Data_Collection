import json
import os
import csv
from pprint import pprint
from pymatgen import MPRester

JINNYAPI = os.environ['materials_project']
m = MPRester(JINNYAPI)

datapath = os.path.abspath('data')

def get_molecules_with_piezo(query):

    data = m.query(criteria=query, properties=["pretty_formula", "material_id", "piezo", "spacegroup.crystal_system"])

    lst = []
    for datum in data:
        if datum['piezo']!= None:
            lst.append((datum["pretty_formula"], datum["material_id"], datum["spacegroup.crystal_system"]))

    print("The query list has been saved.")
    return lst                                                         

def get_csv(lst, filename='with_piezo.csv'):

    with open(filename, mode='w') as file:
        fieldnames = ['pretty_formula', 'material_id', 'spacegroup.crystal_system']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in lst:
            writer.writerow({'pretty_formula': row[0], 'material_id': row[1], 'spacegroup.crystal_system': row[2]})

    print('The csv file has been stored.')


# query = {"elements": {"$all": ["Fe", "O", "H"]}}

query = {}
datalist = get_molecules_with_piezo(query)
get_csv(datalist)