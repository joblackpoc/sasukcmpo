from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('home', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
]