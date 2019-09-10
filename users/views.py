from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm   #we take already exist register form
from django.contrib import messages
from django.contrib.auth.decorators import login_required  #ayto gia na mhn ginetai paraviash ths syndeshs otan patas logout
from .forms import UserRegisterForm

# Create your views here.

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'Your account has been created! You are now able to log in')
      return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form}) 

@login_required        #ayto gia na mhn ginetai paraviash ths syndeshs otan patas logout
def profile(request):
  return render(request, 'users/profile.html')



#synexeia apo 9 lesson