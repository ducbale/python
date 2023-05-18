"""E_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('master/', views.Master, name='master'),
                #   path('', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='index'),
                  path('', views.Index, name='index'),
                  path('signup', views.signup, name='signup'),
                  path('logout_user', views.user_logout, name='user_logout'),
                  path('accounts/login/', LoginView.as_view(template_name='registration/login.html'), name='login'),

                  # Đường dẫn trang hồ sơ
                  path('accounts/profile/', views.profile_view, name='profile'),
                  path('profile',views.u_login,name='profile'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  # add to cart
                  path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
                  path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
                  path('cart/item_increment/<int:id>/',
                       views.item_increment, name='item_increment'),
                  path('cart/item_decrement/<int:id>/',
                       views.item_decrement, name='item_decrement'),
                  path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
                  path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
                  # contact
                  path('contact_us', views.Contact_Page, name='contact_page'),
                  # Check out
                  path('checkout/', views.CheckOut, name='checkout'),

                  # Order page
                  path('order/', views.Your_Order, name='order'),
                  #  Product page
                  path('product/', views.Product_page, name='product'),
                  # Product detail
                  path('product/<str:id>', views.Product_Detail, name='product_detail'),
                  # search
                  path('search/', views.Search, name='search'),
                  path('__debug__/', include('debug_toolbar.urls')),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
