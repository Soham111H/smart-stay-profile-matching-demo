from django.urls import path
from matching import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile_form, name='profile_form'),
    path('matches/', views.matches, name='matches'),
    path('matches/<int:profile_id>/', views.match_detail, name='match_detail'),
    path('profiles/', views.profiles, name='profiles'),
]
