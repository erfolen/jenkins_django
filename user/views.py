from django.shortcuts import render


# Create your views here.
def login(request):
    context = [
    ]
    return render(request, 'user/login.html', context)


def registration(request):
    context = [
    ]
    return render(request, 'user/registration.html', context)


def profile(request):
    context = [
    ]
    return render(request, 'user/profile.html', context)


def logout(request):
    pass
