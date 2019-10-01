from django.urls import path
from . import views 


urlpatterns = [
    path('', views.home,name='peer-home'),
    path('about/',views.about,name='peer-about'),
]
