from django.urls import path
from productos import views
 
   
urlpatterns = [
    path('', views.inicio, name= "inicio"),
    path('snowboard/', views.snowboard, name= "snowboard"),
    path('ski/', views.ski, name= "ski"),
    path('antiparras/', views.antiparras, name= "antiparras")
]
