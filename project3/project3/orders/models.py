from django.db import models

# Create your models here.
class Menu(models.Model):
   food_item = 0 # Link to the available food items

class Topping(models.Model):
   name = models.CharField(max_length=64)
   price = models.DecimalField(max_digits=6, decimal_places=2, default=2.00)

   def __str__(self,):
      return f"{self.name}"

class PizzaType(models.Model):
   REGULAR_PIZZA = "RG"
   SICILIAN_PIZZA = "SI"
   PIZZA_TYPE_CHOICES = (
      (REGULAR_PIZZA, "Regular"),
      (SICILIAN_PIZZA, "Sicilian"),
   )
   
   abbreviation = models.CharField(max_length=2)
   name = models.CharField(max_length = 32)
   price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

   def __str__(self,):
      return f"{self.name}"


class PizzaSize(models.Model):
   SMALL_PIZZA = "SM"
   LARGE_PIZZA = "LG"
   PIZZA_TYPE_CHOICES = (
      (SMALL_PIZZA, "Small"),
      (LARGE_PIZZA, "Large"),
   )

   abbreviation = models.CharField(max_length=2)
   name = models.CharField(max_length = 32)
   price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

   def __str__(self,):
      return f"{self.name}"

class Pizza(models.Model):
   
   pizza_type =  models.ForeignKey(PizzaType, on_delete=models.CASCADE, related_name="type")

   pizza_size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, related_name="size")

   toppings = models.ManyToManyField(to=Topping, blank=True, related_name="pizzas",)

   @property
   price = models.DecimalField(max_digits=6, decimal_places=2, default = ) 

   def __str__(self,):
      # Start with basic pizza information
      retstr = f"{self.pizza_size} {self.pizza_type} Pizza"

      # If there are toppings append to string
      if (self.toppings.all() is not None):
         retstr += f" with "
         for topping in self.toppings.all():
            retstr +=f"{topping}, "
         # Remove final ','
         retstr = retstr[:-2] + " "
         retstr += f"on top"
         
      return retstr

class Sub(models.Model):
   name = models.CharField(max_length=64)

   def __str__(self,):
      return f"{self.name}"

