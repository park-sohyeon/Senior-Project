import socket
import requests

import nxny

def ip_to_xy():
    ip = socket.gethostbyname(socket.gethostname())

    api_key = 'at_2LeH45Xxi8uYgfBQI0FolD2uOBVnx'
    api_url = 'https://geo.ipify.org/api/v2/country,city?'

    url = requests.get(api_url + 'apiKey=' + api_key)
    response = url.json()['location']
    nx, ny = response['lat'], response['lng']
    return nxny.mapToGrid(nx, ny)