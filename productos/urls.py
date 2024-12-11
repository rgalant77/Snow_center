from django.urls import path
from productos import views
 
   
urlpatterns = [
    path('', views.inicio),
    path('snowboard/', views.snowboard),
    path('ski/', views.ski),
    path('antiparras/', views.antiparras)
]
