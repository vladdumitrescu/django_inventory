from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_drones, name='show_drones'),
    path('drone/<int:pk>/', views.drone_details, name='drone'),
    path('add/', views.add_drone, name='add_drone'),
    path('update/<int:pk>', views.update_drone, name='update_drone'),
    path('delete/<int:pk>', views.delete_drone, name='delete_drone'),
    path('search/', views.search_bar, name='search'),
]
