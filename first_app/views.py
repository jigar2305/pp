from django.http import HttpResponse
from django.shortcuts import render
from django.template import context
from .models import users

# Create your views here.


def userdata(request):
    usersx = users.objects.all().values()
    print(usersx)
    userlist = []
    for i in usersx[0].values():
        userlist.append(i)

    print("userlist", userlist)
    context = {
        'usersx': userlist

    }
    return render(request, 'first_app/user.html', context)


def add(request):
    return HttpResponse("user added ..........")


def DeleteData(request):
    d = users.objects.get(userid=2)
    d.delete()
    return HttpResponse("user deleted ..........")


def CreateData(request):
    a = users(username='jigar', email='jigar@gmail.com',
              mobile='96524845', roleid_id=2)
    a.save()
    return HttpResponse("user added ..........")


def UpdateData(request):
    b = users.objects.get(userid=1)
    b.mobile = '123456789'
    b.save()
    return HttpResponse("user updated ..........")
