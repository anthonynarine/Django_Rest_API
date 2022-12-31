from django.apps import AppConfig


class CountriesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "countries"
    
    
    
# DON'T FORGET TO REGISTER THIS APP IN PROJECT SETTINGS

 # countries.apps.CountriesConfig and chorsheaders