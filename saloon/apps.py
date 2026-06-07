from django.apps import AppConfig


class SaloonConfig(AppConfig):
    name = 'saloon'
    
def ready(self):

    import saloon.signals