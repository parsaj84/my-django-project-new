from django.contrib import admin
from .models import *
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["parent", "category"]
    search_fields = ["category"]
    
class FileInProduct(admin.TabularInline):
    model = File
    fields = ["file"]
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "category"]
    inlines = [FileInProduct]


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(File)














# Register your models here.
