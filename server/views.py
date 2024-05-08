from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MealForm,MenuForm
from .models import Restaurant
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request, 'app/index.html')

@login_required
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        description = request.POST.get('description')

        if password == password2:
            if Restaurant.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect('register')
            elif Restaurant.objects.filter(name=name).exists():
                messages.info(request, "Restaurant name already exists")
                return redirect('register')
            else:
                hashed_password = make_password(password)  # Hash the password
                restaurant = Restaurant.objects.create(name=name, email=email, description=description, password=hashed_password)
                restaurant.save()
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')
    else:
        return render(request, 'app/register.html')

# def register(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, "Email already exists")
#                 return redirect('register')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, "Username already exists")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(email=email, username=username, password=password)
#                 user.save()
#                 return redirect('login')
#         else:
#             messages.info(request, "Passwords do not match")
#             return redirect('register')
#     else:
#         return render(request, 'app/register.html')
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Restaurant

# def login(request):
#     return HttpResponse("coming soon")

    
@login_required
def logout(request):
    auth.logout(request)
    return redirect('login')
    # return render(request, 'app/logout.html') 

@login_required 
def dashboard(request,pk):
    UserID = Restaurant.objects.get(id=pk)
    context = {"userID":UserID}
    return render(request, 'app/dashboard.html',{"context":context}) 

@login_required 
def meal(request):
    if request.method == 'POST':
        meal_form = MealForm(request.POST)
        if meal_form.is_valid():
            meal_form.save()
            messages.info(request, "meal has been saved")

            # Optionally, redirect or do something else after saving the form
    else:
        meal_form = MealForm()
    
    context = {'mealForm': meal_form}
    return render(request, 'app/meal.html', context)

# @login_required 
# def order(request):
#     if request.method == 'POST':
#         order_form = OrderForm(request.POST)
#         if order_form.is_valid():
#             order_form.save()
#             # Optionally, redirect or do something else after saving the form
#     else:
#         order_form = OrderForm()
    
#     context = {'orderForm': order_form}
#     return render(request, 'app/order.html', context)


# @login_required 
# def pickup(request):
#     if request.method == 'POST':
#         pickup_form = PickupLocationForm(request.POST)
#         if pickup_form.is_valid():
#             pickup_form.save()
#             # Optionally, redirect or do something else after saving the form
#     else:
#         pickup_form = PickupLocationForm()
    
#     context = {'pickupForm': pickup_form}
#     return render(request, 'app/pickup.html', context)

# @login_required 
# def add_restaurant(request):
    # if request.method == 'POST':
    #     restaurant_form = RestaurantForm(request.POST)
    #     if restaurant_form.is_valid():
    #         restaurant_form.save()
    #         # Optionally, redirect or do something else after saving the form
    # else:
    #     restaurant_form = RestaurantForm()
    
    # context = {'add_restaurantForm': restaurant_form}
    # return render(request, 'app/add_restaurant.html')

def restaurant(request):
    return render(request, 'app/restaurant.html')

def menu_selection(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            selected_items = form.cleaned_data['items']
            # Process the selected items here
    else:
        form = MenuForm()
    return render(request, 'menu_selection.html', {'form': form})                                                                                
