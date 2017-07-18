from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.search_box, name='search_box'),
    #hi
]
