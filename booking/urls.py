from django.urls import path

from booking import views

app_name = 'booking'
urlpatterns = [
    path('', views.index, name='index'),
]