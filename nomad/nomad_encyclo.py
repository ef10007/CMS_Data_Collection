import requests
from config import token
import os
from bs4 import BeautifulSoup

gui_url = 'https://encyclopedia.nomad-coe.eu/gui'
api_access_token = token["token"]["data"]

soup = BeautifulSoup(gui_url)
print(soup)

exit()

# url = 'https://encyclopedia.nomad-coe.eu/api/v1.0/materials/71780' # space group 62
# url = 'https://encyclopedia.nomad-coe.eu/api/v1.0/materials/257771' # space group 221

url = 'https://encyclopedia.nomad-coe.eu/api/v1.0/materials/426707'

os.system('curl -v -u {} {}'.format(api_access_token, url))




# ---------------------------------------------------------------------------------------------------------------------
# r = requests.post(nomad_api_url, auth=(api_access_token, ''), json = {"search_by":{"element":"C", "pagination":"off"}, "has_dos":"true"})

# print(r.status_code) -> 405 Method Not Allowed
# The HyperText Transfer Protocol (HTTP) 405 Method Not Allowed response status code indicates that the request method is known by the server but is not supported by the target resource.

# The server MUST generate an Allow header field in a 405 response containing a list of the target resource's currently supported methods.

# content = r.json()
# print(content)
