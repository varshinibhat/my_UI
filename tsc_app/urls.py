from django.urls import path
from . import views
urlpatterns = [
    #path('',views.index,name="index"),  
    #path('shows/<int:show_id>/characters/', views.show_characters, name='show_characters'),
     path('',views.shows,name="shows"),
     #path('rmc',views.my_view,name="rmc"),
    #path('<int:show_id>/characters/', views.show_characters, name='show_characters'),
    path('/<int:show_id>/characters/', views.show_characters, name='show_characters'),
      #path('characters',views.search_view,name="characters"),
      #path('/insert_shows',views.insert_shows,name='insert_shows'),
      #path('/insert_characters',views.insert_characters,name='insert_characters'),
]