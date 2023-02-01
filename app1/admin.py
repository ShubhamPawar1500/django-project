from django.contrib import admin
from .models import customer, fooditem, reviews

# Register your models here.
admin.site.register(customer)
admin.site.register(reviews)