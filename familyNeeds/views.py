from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import loginForm


# Create your views here.
def login_page(request):
    form = loginForm(request.POST or None)
    errors = []
    context = {
        "form": form,
        "errors": errors
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            print('ok')
            login(request,user)
            return redirect('/needs')
        else:
            pass
    return render(request, 'login.html', context)

def main_router(request):
    if request.user.is_authenticated:
        return redirect("/needs")
    else:
        return redirect("/login")