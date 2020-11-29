import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django_user_agents.utils import get_user_agent
from user.models import DoitUser
from django.contrib.auth import login, authenticate, logout

# Create your views here.
template_name = 'user/login.html'


class LoginView(TemplateView):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('personal-home')
        return render(request, template_name)

    def post(self, request):
        email = request.POST.get("si-mail")
        password = request.POST.get("si-pass")
        if DoitUser.objects.filter(email=email).exists():
            print(f'{email}:{password} user exists.')
            user = authenticate(email=email, password=password)
            if user:
                print('LOGGED IN')
                login(request, user)
                return redirect('personal-home')
            else:
                print('WRONG PASSWORD')
                return render(request, template_name,
                              {'si_mail': email, 'si_pass': password, 'error_msg': 'Wrong Password',
                               'display': 'block'})

        return render(request, template_name, {'si_mail': email, 'si_pass': password})


class RegisterView(TemplateView):

    def get(self, request):
        user_agent = get_user_agent(request)
        if user_agent.is_mobile:
            return render(request, template_name, {'su_opacity': 1, 'su_index': 5})
        else:
            return render(request, template_name, {'panel': 'right-panel-active', })

    def post(self, request):
        return render(request, template_name,
                      {'panel': 'right-panel-active', 'su_mail': f'{request.POST.get("su-mail")}',
                       'su_pass': f'{request.POST.get("su-pass")}', 'su_pass_re': f'{request.POST.get("su-pass-re")}',
                       'su_name': f'{request.POST.get("su-name")}'})


@csrf_exempt
def validate_register(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if DoitUser.objects.filter(email=email).exists():
            response = {'status': 0, 'message': 'Account already exists.', 'url': '/login'}
            return HttpResponse(json.dumps(response), content_type='application/json')
        else:
            DoitUser.objects.create_user(email=email, fullname=name, password=password)


def logout_view(request):
    logout(request)
    return redirect('login')
