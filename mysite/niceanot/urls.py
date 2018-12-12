from django.urls import path

from niceanot import views

app_name = 'niceanot'
urlpatterns = [
    path('', views.index, name='index'),
]