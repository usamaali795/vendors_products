from django.shortcuts import render, get_object_or_404
from .models import Vendor, Product

def vendor_list(request):
    vendors = Vendor.objects.all()
    print(vendors[0].companyDisplayPicture)
    return render(request, 'vendor/vendors_list.html', {'vendors': vendors})

def vendor_detail(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)
    return render(request, 'vendor/vendor_details.html', {'vendor': vendor})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product/product_detail.html', {'product': product})