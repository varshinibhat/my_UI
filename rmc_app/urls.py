from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),  
     #path('hello',views.sec,name="sec"),
     #path('rmc',views.my_view,name="rmc"),
    
      path('characters',views.search_view,name="characters"),
]