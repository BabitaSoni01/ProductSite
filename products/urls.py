from django.urls import path
from . import views as v

urlpatterns = [

    #  Home / Products
    path('', v.home, name='home'),
    path('productlist/', v.productlist, name='productlist'),
    path('product/<int:id>/', v.productdetail, name='productdetail'),

    # Add / Edit / Delete Product
    # path('addproduct/', v.addproduct, name='addproduct'),
    path('editproduct/<int:id>/', v.editproduct, name='editproduct'),
    path('deleteproduct/<int:id>/', v.deleteproduct, name='deleteproduct'),

    # Authentication
    path('login/', v.userlogin, name='login'),
    path('logout/', v.userlogout, name='logout'),

    #  Cart
    path('add-to-cart/<int:id>/', v.add_to_cart, name='add_to_cart'),
    path('cart/', v.cart_view, name='cart'),
    path('remove-from-cart/<int:id>/', v.remove_from_cart, name='remove_from_cart'),


]


# from django.urls import path
# from . import views as v

# urlpatterns = [
#     path('',v.home ,name='home'),
#     path('addproduct/', v.addproduct, name='addproduct'),
#     path('productlist/', v.productlist, name='productlist'),
#     path('editproduct/<int:id>/', v.editproduct, name='editproduct'),
#     path('deleteproduct/<int:id>/', v.deleteproduct, name='deleteproduct'),
#     path('product/<int:id>',v.productdetail,name='productdetail'),
#     path('login/', v.userlogin, name='login'),
#     path('logout/', v.userlogout, name='logout'),
