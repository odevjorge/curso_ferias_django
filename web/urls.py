from django.contrib.auth import views as auth_views
from django.urls import path

from .views import homepage, segunda_pagina

urlpatterns = [
    path("homepage/", homepage, name="homepage"),
    path("segunda_pagina/", segunda_pagina),
    path("login/", auth_views.LoginView.as_view(template_name="auth/login.html"), name='login')
]
