from django.urls import path
from . import views

urlpatterns = [
  path('user-register/', views.user_register, name="user-register-page"),
  path('user-login/', views.user_login, name = 'user-login-page'),
  path('user-logout/', views.user_logout, name = 'user-logout-page'),
  path('user-profile/', views.user_profile, name = 'user-profile-page'),
  path('user-profile-edit/', views.user_profile_edit, name = 'user-profile-edit-page'),
  path('user-change-password/', views.user_change_password, name = 'user-change-password-page'),
  path('user-change-password-two/', views.user_change_password_two, name = 'user-change-password-two-page'),
]
