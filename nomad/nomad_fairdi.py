from bravado.requests_client import RequestsClient
from bravado.client import SwaggerClient
from bravado.exception import HTTPNotFound
from urllib.parse import urlparse
import time
import os
import os.path
import sys

nomad_url = 'https://labdev-nomad.esc.rzg.mpg.de/fairdi/nomad/latest/api'
user = os.environ['nomad_user']
password = os.environ['nomad_pw']

host = urlparse(nomad_url).netloc.split(':')[0]
http_client = RequestsClient()
http_client.set_basic_auth(host, user, password)

client = SwaggerClient.from_url('%s/swagger.json' % nomad_url, http_client=http_client)


# Searching for data
result = client.repo.search(paths='AcAg').response().result
if result.pagination.total == 0:
    print('not found')
elif result.pagination.total > 1:
    print('my ids are not specific enough, bummer ... or did I uploaded stuff multiple times?')
calc = result.results[0]
print(calc)


# Downloading data
client.raw.get(upload_id=calc['upload_id'], path=calc['mainfile']).response()
