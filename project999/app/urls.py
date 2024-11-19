from django.urls import path

from . import views

urlpatterns = [
    
   path('',views.Apiview, name='home'),
   path('create/',views.add_items,name='add-item')
]