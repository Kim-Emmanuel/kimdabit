from django.urls import path
from App import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog, name='blog'),
    path('photos/', views.photos, name='photos'),
    path('footer/', views.current_year, name='current_year'),
]
