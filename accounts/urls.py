from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import home

app_name = "accounts"

urlpatterns = [
    path("", home, name="home"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup_success/", views.SignUpSuccessView.as_view(), name="signup_success"),
    path(
        "login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
            path('logout/', views.logoutView.as_view(), name='logout'),

    
]
