import json
import jq
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)

#     for tenant_admin in data['tenant_admins']:
#         print(tenant_admin['id'])

ids = jq.compile('.tenant_admins[].id').input(data).all()

# Print the extracted names
pprint(ids)
