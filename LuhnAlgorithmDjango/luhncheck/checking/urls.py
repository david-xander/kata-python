from django.urls import path
from . import views


app_name = 'checking'

urlpatterns = [
    path('', views.check_home, name='check_home'),

]