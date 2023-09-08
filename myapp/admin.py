from django.contrib import admin
from .models import Animals,Category
# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('title','category',)
    list_filter=('category',)

class CategoryAdmin(admin.ModelAdmin):
     list_display=('title',)

admin.site.register(Animals,AnimalAdmin)
admin.site.register(Category,CategoryAdmin)