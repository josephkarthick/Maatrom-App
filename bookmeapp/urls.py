from django.urls import path
from .views import  home,save_availability,get_availability

app_name = "bookmeapp"

urlpatterns = [
    path('',home,name='home'),
    path("save_availability/", save_availability, name="save_availability"),   
    path("get_availability/", get_availability, name="get_availability"),    
]