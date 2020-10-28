#!/usr/bin/env python
# posts an update to a firehydrant.io incident timeline from relay

import requests, os
from relay_sdk import Interface, Dynamic as D

relay = Interface()

apiKey = relay.get(D.connection.apiKey),
incidentID = relay.get(D.incidentID)
message = relay.get(D.message)

eventPayload = {
  'body': message,
}

headers = { "Authorization": apiKey }

url = 'https://api.firehydrant.io/v1/incidents/' + incidentID + "/notes"

r = requests.post(url, headers=headers, json=eventPayload)

print('Emitted event to FireHydrant API, got response: ', r.text)

r.raise_for_status()