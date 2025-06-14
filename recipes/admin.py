from django.contrib import admin
from .models import Category, Recipe

# Register your models here.


# 1º maneira de registrar o model 
class CategoryAdmin(admin.ModelAdmin):
    ...


# 2º maneira de registrar o model 
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
