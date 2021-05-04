from django.urls import path
from .import views


urlpatterns = [
    path('', views.all_toys, name='toys'),
    path('<int:toy_id>/', views.toy_details, name='toy_details'),
    path('add/', views.add_toy, name='add_toy'),
    path('edit/<int:toy_id>/', views.edit_toy, name='edit_toy'),
    path(
        'confirm_delete/<int:toy_id>/',
        views.confirm_delete_toy, name='confirm_delete_toy'),
    path('delete/<int:toy_id>/', views.delete_toy, name='delete_toy'),
]
