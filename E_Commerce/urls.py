"""
URL configuration for E_Commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from E_Commerce import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup-form/', views.signup_form, name='signup_form'),
    path('user-signup/', views.user_signup, name='user_signup'),
    path('login-form/', views.login_form, name='login_form'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-logout/', views.user_logout, name='user_logout'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
    path('product-register/', views.product_register, name='product_register'),
    path('edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='delete'),
    path('cart/', views.cart, name='cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('products-api/', views.products_api, name='products_api'),
    path('orders-api/', views.orders_api, name='orders_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
