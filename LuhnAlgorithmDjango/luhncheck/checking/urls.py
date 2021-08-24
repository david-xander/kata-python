from django.urls import path
from . import views


app_name = 'checking'

urlpatterns = [
    path('clients/', views.client_list.as_view(), name='client_list'),
    path('clients/editar/<int:pk>/', views.client_form.as_view(), name='client_edit'),


]