"""ecommerce_store URL Configuration

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
from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.urls import path, include
import store
from store import views


urlpatterns = [
    # Admin APIs
    path('admin/products/', views.ProductListCreateAPIView.as_view(), name='admin-product-list'),
    path('admin/products/<int:pk>/', views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='admin-product-detail'),
    path('admin/orders/', views.OrderListAPIView.as_view(), name='admin-order-list'),
    path('admin/orders/<int:pk>/', views.OrderRetrieveUpdateAPIView.as_view(), name='admin-order-detail'),
    path('admin/users/', views.UserAccountListCreateAPIView.as_view(), name='admin-user-list'),
    path('admin/users/<int:pk>/', views.UserAccountRetrieveUpdateDestroyAPIView.as_view(), name='admin-user-detail'),

    # Customer APIs
    path('products/', views.ProductListAPIView.as_view(), name='customer-product-list'),
    path('users/register/', views.UserRegistrationAPIView.as_view(), name='customer-user-register'),
    path('users/login/', views.UserAuthenticationAPIView.as_view(), name='customer-user-login'),
    path('cart/', views.CartAPIView.as_view(), name='customer-cart'),
    path('cart/items/<int:pk>/', views.CartItemUpdateAPIView.as_view(), name='customer-cart-item-update'),
    path('cart/items/<int:pk>/delete/', views.CartItemDeleteAPIView.as_view(), name='customer-cart-item-delete'),
    path('orders/place/', views.OrderPlacementAPIView.as_view(), name='customer-order-place'),
    path('orders/history/', views.OrderHistoryListAPIView.as_view(), name='customer-order-history'),
]
