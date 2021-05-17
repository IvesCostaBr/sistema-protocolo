from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import TemplateView

# Create your views here.


class Reg(View):
    def get(self, request, *args, **kwargs):
        session = self.request.session.get('abc')
        if session is True:
            print('já esta com carrrinho criado')
        else:
            print('criando carrinho')
            self.request.session['abc'] = True
        return render(request, 'a.html')

    def post(self, request, *args, **kwargs):
        return HttpResponse('post')


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