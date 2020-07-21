import requests
import json
from uuid import getnode as get_mac

endpoint = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyD8BPZ46CIEfJg2LS1hnAsu1vWQlRHbFWw'
mac = get_mac()
mac_address = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))

payload = {
  "considerIp": "true",
  "wifiAccessPoints": [
    {
        "macAddress": mac_address
    }
  ]
}

r = requests.post(endpoint,json=payload)
print(r.text)
#print(r.text)
#request = endpoint + api_key
#print(mac_address)
