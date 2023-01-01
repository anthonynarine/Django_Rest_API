from django.conf.urls import url
from . import views
from  django.urls import path

urlpatterns = [
    path("", views.countries_list),
    path("<int:pk>/", views.countries_detail),

]