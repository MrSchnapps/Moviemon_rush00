from django.urls import path
from .views import MapPageView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('worldmap/', MapPageView.as_view(), name='map')
]
