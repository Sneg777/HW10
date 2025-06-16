from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse, reverse_lazy

from .forms import RegisterForm


class RegisterView(View):
    template_name = 'quotes_auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('quotes_auth:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes_app:home")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                username = form.cleaned_data["username"]
                messages.success(request, f"Good job {username}, you are registered")
                return redirect(self.success_url)
            except Exception as e:
                messages.error(request, f"Registration error: {str(e)}")
                print(f"Error saving user: {e}")
        else:
            print("Form errors:", form.errors)
        return render(request, self.template_name, {"form": form})
