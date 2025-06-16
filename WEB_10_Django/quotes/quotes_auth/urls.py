from django.urls import path, include
from .views import RegisterView
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm

app_name = 'quotes_auth'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name='quotes_auth/login.html', form_class=LoginForm,
                                     redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

]
