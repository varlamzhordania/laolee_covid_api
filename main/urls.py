from django.urls import path
from .views import covid_case_list, covid_case_detail

app_name = 'main'

urlpatterns = [
    path('covid/', covid_case_list, name='covidcase-list'),
    path('covid/<int:pk>/', covid_case_detail, name='covidcase-detail'),
]
