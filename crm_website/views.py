from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# home function is a Django view that takes in the HTTP request and
# renders the 'home.html' template and returns it as an HTTP response.
def home(request):
    # basically takes all the records from model.records and passes it into the webpage
    # as a dictionary with the URL kinda ig
    records = Record.objects.all()

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
        # if there are no records i.e user hasn't already logged in then it will render without records
        return render(request, 'home.html', {'records':records})


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

def customer_record(request,pk):
    if request.user.is_authenticated:
        # Get records from our models, using the id crated by our migrations file
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be logged in to view record")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record deleted successfully!!!")
        return redirect('home')
    else:
        messages.success(request,"You must be logged in to perform this action.")
        return redirect('home')
    
def add_record(request,pk):
    return render(request, 'record.html', {'customer_record':customer_record})
