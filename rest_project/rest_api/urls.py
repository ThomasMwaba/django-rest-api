from django.urls import path

from . import views


urlpatterns = [
    path('planets',views.planet_list, name='planets'),
    path('planet/<int:pk>',views.planet,name='planet'),
]