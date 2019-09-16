import json
import requests
import os
from pprint import pprint

JINNYAPI = os.environ['materials_project']
#  https://www.materialsproject.org/rest/v1/materials/Fe2O3/exp

# URL = "https://www.materialsproject.org/rest/v2/materials/*3O4/vasp/piezo"

URL = 'https://www.materialsproject.org/rest/v1/materials/CMgN2'
r = requests.get(URL,
                 headers={"X-API-KEY": os.environ['materials_project']})

content = r.json() # a dict
pprint(content["response"])