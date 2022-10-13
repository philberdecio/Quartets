from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('folios/', views.FolioList.as_view(), name="folios"),
    path('quartets/', views.Quartets.as_view(), name="quartets"),
    path('folios/new/', views.FolioCreate.as_view(), name="new_folio"),
    path('folios/<int:pk>/', views.FolioDetail.as_view(), name="folio_detail"),
    path('folios/<int:pk>/update', views.FolioUpdate.as_view(), name="folio_update"),
    path('folios/<int:pk>/delete', views.FolioDelete.as_view(), name="folio_delete"),

]