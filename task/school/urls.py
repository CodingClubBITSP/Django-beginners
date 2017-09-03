from django.conf.urls import url
from .import views

app_name = 'school'

urlpatterns = [

    url(r'^$', views.main, name='main'),
    url(r'^grace/$', views.grace, name='grace'),

]