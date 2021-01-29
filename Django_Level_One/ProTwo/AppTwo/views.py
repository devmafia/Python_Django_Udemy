from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
from AppTwo import forms

def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    help = {'help': 'Help page'}
    return render(request, 'AppTwo/help.html', context=help)

def users(request):
    wpg_list = Users.objects.order_by('first_name')
    users_dict = {'access_users': wpg_list}
    return render(request, 'AppTwo/users.html', context=users_dict)

def forms_page(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print('Name: '+form.cleaned_data['first_name'])
            print('Email: '+form.cleaned_data['email'])
            form.save(commit=True)
            return index(request)
    return render(request, 'AppTwo/forms.html.', {'forms': form})
# Create your views here.
