from django.urls import path
from .views import post_list,add_post,delete

app_name='posts'

urlpatterns = [
    path('',post_list,name='post_list'),
   path('addpost',add_post,name='add_post'),

    

    path('delete-post',delete,name='delete-post'),
   
    


  
]
