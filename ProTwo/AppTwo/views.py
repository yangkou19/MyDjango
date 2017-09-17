from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import Users
# Create your views here.
def index(request):
    return HttpResponse("<em>My Pro Two</em>")

def users(request):
    user_list = Users.objects.order_by('last_name')
    user_dict = {'users': user_list}
    return render(request, 'AppTwo/users.html', context = user_dict)

def help(request):
    helpdict = {'help_insert': 'HELP PAGE'}
    return render(request, 'AppTwo/help.html', context = helpdict)
