from django.shortcuts import render, redirect
from .models import customer, fooditem, reviews
from .forms import create_customer, create_food, create_review, Userform
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(req):
     abc = reviews.objects.all().values()
     return render(req, 'home.html', {'review':abc})

def user_page(req):
     abc = customer.objects.all().values()
     return render(req, 'uesr.html', {'user':abc})

def upload_user(req):
     if req.method == 'POST':
          abc = create_customer(req.POST)
          if abc.is_valid():
               abc.save()
               return redirect('home')
          else:
               return HttpResponse('Invaild credentials')
     else:
          abc = create_customer()
     return render(req, 'upload_user.html', {'upload':abc})

def edit_user(req, name):
     name = str(name)
     try:
          user_sel = customer.objects.get(username=name)
     except customer.DoesNotExist:
          return redirect('user')
     else:
          abc = create_customer(req.POST or None, instance=user_sel)
          if abc.is_valid():
               abc.save()
               return redirect('user')
     return render(req, 'upload_user.html', {'upload':abc})

def del_user(req, name):
     name = str(name)
     try:
          user_sel = customer.objects.get(username=name)
     except customer.DoesNotExist:
          return redirect('user')
     else:
          user_sel.delete()
          return redirect('user')

def food_page(req):
     abc = fooditem.objects.all().values()
     return render(req, 'food.html', {'food':abc})

def upload_food(req):
     if req.method == 'POST':
          abc = create_food(req.POST)
          if abc.is_valid():
               abc.save()
               return redirect('foodpage')
          else:
               return HttpResponse('Invaild credentials')
     else:
          abc = create_food()
     return render(req, 'upload_food.html', {'upload':abc})

def upload_review(req):
     if req.method == 'POST':
          abc = create_review(req.POST)
          if abc.is_valid():
               abc.save()
               return redirect('home')
          else:
               return HttpResponse('Invaild credentials')
     else:
          abc = create_review()
     return render(req, 'upload_review.html', {'upload':abc})

def edit_food(req, id):
     id = int(id)
     try:
          food_sel = fooditem.objects.get(id=id)
     except customer.DoesNotExist:
          return redirect('foodpage')
     else:
          abc = create_food(req.POST or None, instance=food_sel)
          if abc.is_valid():
               abc.save()
               return redirect('foodpage')
     return render(req, 'upload_food.html', {'upload':abc})

def del_food(req, id):
     id = str(id)
     try:
          food_sel = fooditem.objects.get(id=id)
     except fooditem.DoesNotExist:
          return redirect('foodpage')
     else:
          food_sel.delete()
          return redirect('foodpage')

def edit_rating(req, id):
     id = int(id)
     try:
          rating_sel = reviews.objects.get(id=id)
     except reviews.DoesNotExist:
          return redirect('home')
     else:
          abc = create_review(req.POST or None, instance=rating_sel)
          if abc.is_valid():
               abc.save()
               return redirect('home')
     return render(req, 'upload_review.html', {'upload':abc})

def del_rating(req, id):
     id = str(id)
     try:
          rating_sel = reviews.objects.get(id=id)
     except reviews.DoesNotExist:
          return redirect('home')
     else:
          rating_sel.delete()
          return redirect('home')

def register(req):
     if req.method == "POST":
          abc = Userform(req.POST)
          if abc.is_valid():
               user = abc.save()
               login(req, user)
               return redirect('home')
          else:
               return HttpResponse('Invalid credentials')
     else:
          abc = Userform()
     return render(req, 'register.html', {'register':abc})

def logout_request(req):
     logout(req)
     return redirect('/')

def login_request(req):
     if req.method == 'POST':
          abc = AuthenticationForm(req, data=req.POST)
          if abc.is_valid():
               username = abc.cleaned_data.get('username')
               password = abc.cleaned_data.get('password')
               user = authenticate(username=username, password=password)
               if user is not None:
                    login(req, user)
                    return redirect('home')
               else:
                    return HttpResponse('invalid')
          else:
               return HttpResponse('invalid')
     abc = AuthenticationForm()
     return render(req, 'login.html', {'login':abc})