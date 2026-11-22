from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product,Cart


# Create your views here.
def home(request):
    data=Product.objects.all()
    con={'products':data}
    return render(request,'home.html',con)

# @login_required
# def addproduct(request):
#     if request.method=='POST':
#         form=ProductForm(request.POST,request.FILES)
#         form.save()
#         return redirect('/')
#     else:
#         form=ProductForm()
#         con={'form':form}
#         return render(request,'addproduct.html',con)
    
# def productlist(request):
#     products = Product.objects.all().order_by('-id')
#     return render(request, 'productlist.html', {'products': products})

from .models import Product, Category

@login_required
def productlist(request):
    q = request.GET.get('q')
    cat = request.GET.get('category')
    products = Product.objects.all()
    if q:
        products = products.filter(name__icontains=q)

    if cat:
        products = products.filter(category__id=cat)

    categories = Category.objects.all()
    return render(
        request,
        'productlist.html',
        {'products': products, 'categories': categories}
    )


# def deleteproduct(request,id):
#     inc=Product.objects.get(id=id)
#     inc.delete()
#     return redirect('productlist')

def deleteproduct(request, id):
    product = get_object_or_404(Product, id=id)  # ✅ yahi fix hai

    if request.method == "POST":
        product.delete()
        return redirect('productlist')

    return render(request, 'confirmdelete.html', {'product': product})


def editproduct(request,id):
    inc=Product.objects.get(id=id)
    if request.method=="POST":
        f=ProductForm(request.POST,request.FILES,instance=inc)
        f.save()
        return redirect('productlist')
    else:
        f=ProductForm(instance=inc)
        content={'form':f}
        return render(request,'editproduct.html',content)
    
def productdetail(request,id):
    product=Product.objects.get(id=id)
    con={'product':product}
    return render(request,'productdetail.html',con)
    
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('productlist')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def userlogout(request):
    logout(request)
    return redirect('login')

@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)

    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def remove_from_cart(request, id):
    cart_item = get_object_or_404(Cart, id=id, user=request.user)
    cart_item.delete()
    return redirect('cart')
