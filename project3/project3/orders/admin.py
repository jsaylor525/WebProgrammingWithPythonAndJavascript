from django.contrib import admin

# Register your models here.
from .models import Menu, Pizza, Topping, Sub, PizzaSize, PizzaType

# Register your models here.
admin.site.register(Menu)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(PizzaSize)
admin.site.register(PizzaType)