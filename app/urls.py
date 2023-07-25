from django.urls import path
from  . import views


urlpatterns = [
    path('', views.home, name='index'),
    path('property', views.property_list, name = 'property_list'),
    path('<int:id>', views.property_detail, name = 'property_detail'),
 ]
