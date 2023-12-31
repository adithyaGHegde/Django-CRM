from django.urls import path
from . import views

# need to connect our URLs to views from the views.py file
urlpatterns = [
    path('',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('record/<int:pk>',views.customer_record,name='record'),
    path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
    path('add_record/',views.add_record,name='add_record'),
]
