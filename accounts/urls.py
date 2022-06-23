from django.urls import path
from .views import login_view, logout_view, registration_view, profile, ProfileUpdate

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registration_view, name='register'),
    path('profile/<int:pk>', profile, name='profile'),
    path('profile/update/<int:pk>', ProfileUpdate.as_view(), name='profile_update'),
]