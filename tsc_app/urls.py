from django.urls import path
from . import views
urlpatterns = [
    #path('',views.index,name="index"),  
     path('',views.shows,name="sec"),
     #path('/shows',views.shows,name="shows"),
     #path('rmc',views.my_view,name="rmc"),
    
      #path('characters',views.search_view,name="characters"),
]