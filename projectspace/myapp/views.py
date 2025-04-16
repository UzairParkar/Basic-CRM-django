from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
# Create your views here.
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #authenticate 
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You have been logged in')
            return redirect('home')
        else:
            messages.error(request,'There was an error logging in try again later.')
            return redirect('home')
    else:
        return render(request,'home.html',{'records':records})


#request is sent back to the back and  returns a response. 
#it is a three step cycle
#1. request
#2. URL
#3. VIEW

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,'logged out sucessfully')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            #form.cleaned_data pulls out the username and password from the registeration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'logged in sucessfully')
            return redirect('home')
    else:
        form = SignUpForm() 
        return render(request,'register.html',{'form':form})
    return render(request,'register.html',{'form':form})


def detail_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        if customer_record:
            messages.success(request,'here is your record....')
            return render(request,'details.html',{'customer_records':customer_record})  

def delete_record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        customer_record.delete()
        messages.success(request,'deleted the record sucessfully')
        return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Record Added...")
				return redirect('home')
		return render(request, 'create.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')
     

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
        #makes sure that the existing records are there in the input fields
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('home')
		return render(request, 'update.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')