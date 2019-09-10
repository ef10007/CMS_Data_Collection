import json
import requests
import os
from pprint import pprint

JINNYAPI = os.environ['materials_project']


r = requests.get("https://www.materialsproject.org/rest/v2/materials/*3O4/vasp/piezo",
                 headers={"X-API-KEY": os.environ['materials_project']})
content = r.json() # a dict
pprint(content["response"])