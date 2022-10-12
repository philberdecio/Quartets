from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('folios/', views.FolioList.as_view(), name="folios"),
    path('quartets/', views.Quartets.as_view(), name="quartets")
]