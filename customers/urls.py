

from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('_index', views.index, name='index'),
    path('success', views.successSendMail, name='success'),
]
