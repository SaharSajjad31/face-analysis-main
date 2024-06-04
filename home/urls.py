# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('img-del/<pk>/', views.ImageDeleteView.as_view(), name='img_del'),
    path('index/<str:courseid>/', views.Images, name='images'),
    path('chat/', views.ChatView.as_view(), name='chat'),
    path('analysis/<int:image_id>/', views.analysis_view, name='analysis'),
    path('display-images/', views.display_img, name='display_img'),  # For display_img
    path('display-images/<str:dominant_race>/<str:dominant_gender>/', views.display_images, 
         name='display_images'),  # For display_images with parameters
    path('contact/', views.contact_page, name='contact'),
    path('history/', views.history_page, name='history'),
    
    

]
