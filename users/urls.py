from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_user, name="register"),
    path("profile/", views.user_profile, name="profile"),
    path("login/", views.login_user, name="login"),
    path("fb_profile/", views.fetch_facebook_user_profile, name="fb_profile")
    # Other URL patterns
]
