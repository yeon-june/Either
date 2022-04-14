from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'votes'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('<int:pk>/detail_result', views.detail_result, name='detail_result'),
    path('<int:pk>/create_comment', views.create_comment, name='create_comment'),
    path('<int:pk>/delete', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)