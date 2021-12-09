from django.urls import path

from . import views

app_name = 'winRate'

urlpatterns = [
    path('', views.home, name='home'),

]
