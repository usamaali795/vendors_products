from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.vendor_list, name='vendor_list'),
    path('vendor/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout')


]
