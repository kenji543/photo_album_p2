from django.urls import path

from . import views

urlpatterns = [
    path('', views.AlbumListView.as_view(), name='album_list'),
    path('albums/new/', views.AlbumCreateView.as_view(), name='album_create'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album_detail'),
    path('albums/<int:pk>/edit/', views.AlbumUpdateView.as_view(), name='album_edit'),
    path('albums/<int:pk>/delete/', views.AlbumDeleteView.as_view(), name='album_delete'),
    path('albums/<int:pk>/photos/upload/', views.PhotoCreateView.as_view(), name='photo_upload'),
    path('photos/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('contact/', views.ContactCreateView.as_view(), name='contact'),
    path('contact/thanks/', views.ContactThanksView.as_view(), name='contact_thanks'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
