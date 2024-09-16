from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def signup(request):
    signupForm=UserCreationForm(request.POST or None)
    if signupForm.is_valid():
        signupForm.save()
        username=signupForm.cleaned_data.get('username')
        raw_password=signupForm.cleaned_data.get('password1')
        user=authenticate(username=username,password=raw_password)
        login(request, user)
        return redirect('viewdlm')
    return render(request, 'signup.html',{'form':signupForm})





