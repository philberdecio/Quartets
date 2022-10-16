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
    path('folios/<int:pk>/new/', views.QuartetCreate.as_view(), name="new_quartet"),
    path('folios/<int:folio_pk>/<int:pk>', views.QuartetDetail.as_view(), name="quartet_detail"),
    path('folios/<int:folio_pk>/<int:pk>/update', views.QuartetUpdate.as_view(), name="quartet_update"),
    path('folios/<int:folio_pk>/<int:pk>/delete', views.QuartetDelete.as_view(), name="quartet_delete"),
    path('folios/<int:folio_pk>/<int:pk>/new_text_entry/', views.TextEntryCreate.as_view(), name="new_text_entry"),
    path('folios/<int:folio_pk>/<int:pk>/new_image_entry/', views.ImageEntryCreate.as_view(), name="new_image_entry"),
    path('folios/<int:folio_pk>/<int:pk>/new_embed_entry/', views.EmbedEntryCreate.as_view(), name="new_embed_entry"),
    path('folios/<int:folio_pk>/<int:pk>/new_video_entry/', views.VideoEntryCreate.as_view(), name="new_video_entry"),
]