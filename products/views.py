from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm

def product_list(request):
    categories = Category.objects.all()
    featured_products = Product.objects.filter(featured=True)
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {
        'products': products, 
        'categories': categories,
        'featured_products': featured_products
    })

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    
    # Add to cart form
    cart_product_form = CartAddProductForm()
    
    return render(request, 'products/product_detail.html', {
        'product': product,
        'related_products': related_products,
        'cart_product_form': cart_product_form
    })
    
def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'products/category_products.html', {
        'category': category,
        'products': products,
        'categories': categories
    })
