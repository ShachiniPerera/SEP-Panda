from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    allergen = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    dairy_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    preparation_time = models.PositiveIntegerField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    specials = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    
    @property
    def availability(self):
        if self.available:
            return "Available"
        else:
            return "Not-Available"
        
    @property
    def speciality(self):
        if self.specials:
            return "Yes"
        else:
            return "No"
