from django.urls import path

from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('planets',views.planet_list, name='planets'),
    path('planet/<int:pk>',views.planet,name='planet'),
    path('register',views.register,name='register'),
    
    path('login',obtain_auth_token,name='login'),
]