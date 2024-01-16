from .models import Product
from django.forms import ModelForm

class ProductForm(ModelForm):
     class Meta:
         model = Product
         fields = ['product_name', 'category', 'subcategory', 'price', 'desc', 'pub_date', 'image']