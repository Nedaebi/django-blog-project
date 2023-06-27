from django.urls import  path
from .views import  PostUpdateView, PostCreatVeiew, PostDeleteView,PostListView,PostDetailView

urlpatterns= [

    path('', PostListView.as_view(), name= "posts_list"),
     path('<int:pk>/',PostDetailView.as_view(), name= "post_detail"),
     path('add/',PostCreatVeiew.as_view(), name= "add_new_post"),
     path('<int:pk>/update/', PostUpdateView.as_view(),name='post_update' ), 
     path('<int:pk>/delete/', PostDeleteView.as_view(),name='post_delete')

]