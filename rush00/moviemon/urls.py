from django.urls import path
from .views import MapPageView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('worldmap/', MapPageView.as_view(), name='map'),
    path('moveup/', views.moveup, name='up'),
    path('movedown/', MapPageView.as_view(), name='down'),
    path('moveleft/', MapPageView.as_view(), name='left'),
    path('moveright/', MapPageView.as_view(), name='right')
]
