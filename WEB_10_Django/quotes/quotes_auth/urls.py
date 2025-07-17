from django.urls import path, include
from .views import RegisterView, AuthenticatedPasswordResetView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from .forms import LoginForm
from django.urls import reverse_lazy

app_name = 'quotes_auth'

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name='quotes_auth/login.html', form_class=LoginForm,
                                     redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('password_change/', PasswordChangeView.as_view(
        template_name='quotes_auth/password_change_form.html',
        success_url=reverse_lazy('quotes_auth:password_change_done')), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='quotes_auth/password_change_done.html'), name='password_change_done'),

    path('password-reset/',
         AuthenticatedPasswordResetView.as_view(), name='password_reset'),

    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='quotes_auth/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='quotes_auth/password_reset_confirm.html',
             success_url='/auth/reset/complete/'
         ),
         name='password_reset_confirm'),

    path('reset/complete/',
         PasswordResetCompleteView.as_view(
             template_name='quotes_auth/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
