from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm

# home function is a Django view that takes in the HTTP request and
# renders the 'home.html' template and returns it as an HTTP response.
def home(request):

    # Check to see if user is logging in i.e if there is a POST request from
    # the form: it has its method POST so you can access the fields in it by 
    # their names
    if request.method == 'POST':
        username  = request.POST['user_name']
        password  = request.POST['password']

        # Authenticate
        user= authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request,"There was an error logging in, Please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request,"You've been logged out")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user  = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
        
    return render(request, 'register.html', {'form':form})