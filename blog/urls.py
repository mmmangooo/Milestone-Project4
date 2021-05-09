from django.urls import path
from .import views


urlpatterns = [
    path('', views.blog, name='blog'),
    path(
        'blog_details/<int:blogpost_id>/',
        views.blog_details, name='blog_details'),
    path('add/', views.add_blogpost, name='add_blogpost'),
    path('edit/<int:blogpost_id>/', views.edit_blogpost, name='edit_blogpost'),
    path(
        'confirm_delete/<int:blogpost_id>/',
        views.confirm_delete_blogpost, name='confirm_delete_blogpost'),
    path(
        'delete/<int:blogpost_id>/',
        views.delete_blogpost, name='delete_blogpost'),
]
