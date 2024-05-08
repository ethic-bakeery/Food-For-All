from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Payment
from django.db.models import Q 
from server.models import Restaurant

def index(request):
    return render(request, 'client/index.html')

def register(request):
    if request.method == "POST":
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already exists")
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'client/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid credentials")
            return render(request, 'client/login.html') 
    else:
        return render(request, 'client/login.html') 
    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
#     # return render(request, 'app/logout.html') 

@login_required 
def home(request):
    q = request.POST.get('q', '')  # Use get() with default value instead of if condition
    restaurants = []
    if q:
        restaurants = Restaurant.objects.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        )
    context = {'restaurants': restaurants, 'query': q}
    
    return render(request, 'client/home.html', context)
@login_required 
def transaction(request):
    if request.method == 'POST':
        transaction_form = Payment(request.POST)
        if transaction_form.is_valid():
            transaction_form.save()
            # Optionally, redirect or do something else after saving the form
    else:
        transaction_form = Payment()
    
    context = {'transactionForm': transaction_form}
    return render(request, 'client/transaction.html', context)      