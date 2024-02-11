from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password , check_password
from product.models import Product
from category.models import Category
from order.models import Order


def signup_form(request):
    context = {}
    return render(request, 'signup.html', context)

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_in_process = request.POST.get('password')
        password = make_password(password_in_process)
        user = User(username=username, email=email, password=password)
        user.save()
        login(request, user)
        return redirect('index')
    return redirect('index')

def login_form(request):
    context = {}
    return render(request, 'login.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['customer'] = user.id
            return redirect('index')
        else:
              return render(request, 'login.html', {"error": "Email or password is invalid"})
    return redirect('index')

def user_logout(request):
    logout(request)
    return redirect('login_form')


def index(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.method == 'GET':
        category_id = request.GET.get('category')
        search_product = request.GET.get('searchproduct')
        if search_product != None:
            products = Product.objects.filter(description__icontains = search_product)
        if category_id:
            products = Product.objects.filter(category_id = category_id)
    context ={'products': products, "categories": categories}
    return render(request, 'index.html', context)


def admin_panel(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    if request.method == 'GET':
        category_id = request.GET.get('category')
        search_product = request.GET.get('searchproduct')
        if search_product != None:
            products = Product.objects.filter(description__icontains = search_product)
        if category_id:
            products = Product.objects.filter(category_id = category_id)
    context ={'products': products, "categories": categories}
    return render(request, 'admin.html', context)


def product_register(request):
    if request.method == 'POST':
        product_name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        product = Product(name=product_name, description=description, price=price, image=image, category_id=category)
        product.save()
    return redirect('admin_panel')


def edit(request, id):
    if request.method == 'POST':
        product_name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        category = request.POST.get('category')
        image = request.FILES.get('image')
        product = Product(id =id,name=product_name, description=description, price=price, image=image, category_id=category)
        product.save()
    return redirect('admin_panel')

def delete(request, id):
        product = Product.objects.filter(id =id)
        product.delete()
        return redirect('admin_panel')

def cart(request):
    if request.method == 'POST':
       product =  request.POST.get("product")
       remove =  request.POST.get("remove")
       cart = request.session.get('cart')
       if cart:
           quantity = cart.get(product)
           if quantity:
                if remove:
                    if quantity <=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
           else:
               cart[product] = 1
       else:
           cart = {}
           cart[product] = 1
       request.session['cart'] = cart
       print(request.session['cart'])
    return redirect('index')

def view_cart(request):
    ids = list(request.session.get('cart').keys())
    products = Product.get_product_by_id(ids)
    print(products)
    context = {"products":products}
    return render(request, 'cart.html', context)


def checkout(request):
        if request.method == 'POST':
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            customer = request.session.get('customer')
            cart = request.session.get('cart')
            products = Product.get_product_by_id(list(cart.keys()))
            for product in products:
                order = Order(quantity=cart.get(str(product.id)), price=product.price, customer=User(id=customer), product=product, address=address, phone=phone)
                order.place_order()
                request.session['cart'] = {}
        return redirect('view_cart')


def orders(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    customer = request.session.get("customer")
    orders = Order.objects.filter(customer=customer).order_by("-date")
    context = {
        "orders": orders,
        "products": products,
        "categories": categories
    }
    return render(request, 'orders.html', context)