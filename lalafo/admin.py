from django.contrib import admin
from .models import Lalafo, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Lalafo)
class LalafoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'created')
