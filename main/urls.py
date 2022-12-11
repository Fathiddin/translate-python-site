from django.urls import path
from .import views

app_name="main"

urlpatterns=[
    path('', views.home, name='home'),
    path('list/', views.list, name='list'),
    path('add/', views.add, name='add'),
    path('added/', views.addlist, name='addlist'),
    path("search/", views.search, name='search'),
]