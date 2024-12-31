from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('post_list', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('comment/<int:comment_id>/reply/', views.add_reply, name='add_reply'),
]