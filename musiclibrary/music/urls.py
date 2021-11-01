from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:pk>/', views.SongDetails.as_view()),
    path('music/<int:pk>/like/', views.SongLike.as_view()),
]