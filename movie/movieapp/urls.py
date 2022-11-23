from django.urls import path
from . import views

app_name = 'movieapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('details/<int:id>/', views.details, name="details"),
    path("update/<int:movie_id>/", views.update, name="update"),
    path("add/", views.add, name="add"),
    path("delete/<int:id>/", views.delete, name="delete"),
    
]
