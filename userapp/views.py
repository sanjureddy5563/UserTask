from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['psw']
        user_data = User(username=username,email=email)
        user_data.set_password(password)
        user_data.save()
        return redirect('login')
    return render(request,'register.html')

def add_product(request):
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_type = request.POST['product_type']
        product_location = request.POST['product_location']
        user_data = request.user
        prod_data = Product(product_name=product_name,product_price=product_price,product_type=product_type,product_location=product_location,user=user_data)
        prod_data.save()
        return redirect('list_product')
    return render(request,'add_product.html')


def list_product(request):
    product_data = Product.objects.filter(user=request.user)
    return render(request,'list_product.html',{'prod_list':product_data})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        is_auth = authenticate(username=username,password=password)
        if is_auth is None:
            return redirect('login')
        else:
            login(request,is_auth)
            return redirect('list_product')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')
