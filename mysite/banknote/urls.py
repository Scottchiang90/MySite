from django.urls import path

from banknote.views import AppraisalDetail
from booking import views

app_name = 'banknote'
urlpatterns = [
    path('appraisals/<id_num>/', AppraisalDetail.as_view(), name='author-detail'),
]