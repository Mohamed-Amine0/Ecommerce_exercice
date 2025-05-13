from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Icon class name (ex: fas fa-tools)")
    
    class Meta:
        verbose_name_plural = "Categories"
        
    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('products:category_products', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Afficher ce produit en page d'accueil")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id])
