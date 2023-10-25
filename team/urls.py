from django.urls import path

from . import views

app_name = 'team'
urlpatterns = [
    path('', views.teams_list, name='list'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit', views.team_edit, name='edit'),
    path('<int:pk>/activate', views.team_activate, name='activate'),
]
