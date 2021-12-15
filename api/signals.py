from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Location
from .utils import get_client_data

@receiver(pre_save,sender=Location)
def add_data(sender,instance,*args,**kwargs):

    # lets assume that we want to get data if the user passes only IP, it means that there is neither latitude nor longitude

    if not instance.latitude or instance.longitude:
        client_data=get_client_data(instance.ip)
        instance.ip_type =client_data['ip_type']
        instance.continent_code=client_data['continent_code']
        instance.continent_name=client_data['continent_name']
        instance.country_code=client_data['country_code']
        instance.country_name=client_data['country_name']
        instance.region_code=client_data['region_code']
        instance.region_name=client_data['region_name']
        instance.city=client_data['city']
        instance.zip_code=client_data['zip_code']
        instance.latitude=client_data['latitude']
        instance.longitude=client_data['longitude']
    
