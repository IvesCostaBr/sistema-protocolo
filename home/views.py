from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.

class RegistrarLogin(TemplateView):
    template_name = 'registration/sig_in.html'

    def post(self, request):
        if self.request.method == 'POST':
            username = self.request.POST['username']
            email = self.request.POST['email']
            if self.request.POST['password1'] == self.request.POST['password2']:
                password = self.request.POST['password1']
            User.objects.create_user(username, email, password)
        return redirect('login')






def homepage(request):
    return render(request, 'home.html')