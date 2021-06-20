from django.urls import path
from .views import MapPageView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('worldmap/', MapPageView.as_view(), name='map'),
    path('moveup/', views.moveup, name='up'),
    path('movedown/', views.movedown, name='down'),
    path('moveleft/', views.moveleft, name='left'),
    path('moveright/', views.moveright, name='right')
]
