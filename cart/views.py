"""
Views for the cart application.

These views handle the cart functionality:
- Adding products to cart
- Removing products from cart
- Updating product quantities
- Displaying cart contents
- Clearing the entire cart
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from django.contrib import messages
from products.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
        
        if cd['update']:
            messages.success(request, f'Quantité de "{product.name}" mise à jour!')
        else:
            messages.success(request, f'"{product.name}" a été ajouté à votre panier!')
    
    # Redirect to the referring page if available, otherwise go to cart
    referring_page = request.META.get('HTTP_REFERER')
    if referring_page and 'cart' not in referring_page:
        return redirect(referring_page)
    else:
        return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, f'"{product.name}" a été retiré de votre panier!')
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'update': True}
        )
    return render(request, 'cart/cart_detail.html', {'cart': cart})
    
@require_POST
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    messages.success(request, 'Votre panier a été vidé!')
    return HttpResponse(status=200)
