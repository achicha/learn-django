from django.contrib import auth
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response, redirect


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)       # uer auth
            return redirect('/')
        else:
            args['login_error'] = 'user not found'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')
