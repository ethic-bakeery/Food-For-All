from . import views
from django.urls import path 

app_name = 'client'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),  #
    path('home/', views.home, name='home'),  
    path('login/', views.login, name='login'),  
    path('transaction/', views.transaction, name='transaction'),  
]
