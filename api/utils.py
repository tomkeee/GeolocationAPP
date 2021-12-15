import requests
import json

from root.sensitive import API_KEY
from .models import Location

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip
    
def get_client_data(ip):
    url=f"http://api.ipstack.com/{ip}/?access_key={API_KEY}"
    response=requests.get(url)
    data=response.text
    parse_json=json.loads(data)

    client_data={
        'ip':parse_json['ip'],
        'ip_type':parse_json['type'],
        'continent_code':parse_json['continent_code'],
        'continent_name':parse_json['continent_name'],
        'country_code':parse_json['country_code'],
        'country_name':parse_json['country_name'],
        'region_code':parse_json['region_code'],
        'region_name':parse_json['region_name'],
        'city':parse_json['city'],
        'zip_code':parse_json['zip'],
        'latitude':parse_json['latitude'],
        'longitude':parse_json['longitude']
    }
    return client_data

def save_client_data(ip):
    client_data=get_client_data(ip)

    x=Location.objects.create(
        ip=client_data['ip'],
        ip_type=client_data['ip_type'],
        continent_code=client_data['continent_code'],
        continent_name=client_data['continent_name'],
        country_code=client_data['country_code'],
        country_name=client_data['country_name'],
        region_code=client_data['region_code'],
        region_name=client_data['region_name'],
        city=client_data['city'],
        zip_code=client_data['zip_code'],
        latitude=client_data['latitude'],
        longitude=client_data['longitude']
    )
    return x
