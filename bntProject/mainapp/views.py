from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home(request):
  return render(request, 'index.html')


# Registration of new users
def sign_up(request, *args, **kwargs):
  reg_form = RegisterForm
  if request.method == 'POST':
    reg_form = RegisterForm(request.POST or None)
    if reg_form.is_valid():
      reg_form.save()
      return redirect('signIn')
   context = {
     'form':reg_form,
   }
  return render(request, 'sign_up.html', context)

# I was thinking of handling this login post & get request with AJAX but will do it later
def sign_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            user1 = request.user
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Email OR password is incorrect')

    context = {}
    return render(request, 'sign_in.html', context)


def sign_out(request, pk='fullname'):
    # context={'num':num}
    logout(request)
    return redirect('signIn')
