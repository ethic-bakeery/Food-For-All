from . import views
from django.urls import path 

app_name = 'server'

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    # path('login', views.login, name='login'),
    path('dashboard/<str:pk>/', views.dashboard, name='pk'),
    path('logout', views.logout, name='logout'),
    path('meal', views.meal, name='meal'),
    # path('order', views.order, name='order'),
    path('menu_selection', views.menu_selection, name='menu_selection'),
    # path('add_restaurant', views.add_restaurant, name='add_restaurant'),
    path('restaurant', views.restaurant, name='restaurant')

]               