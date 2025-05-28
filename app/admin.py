from django.contrib import admin

# Register your models here.
from .models import Tags, Blog,Comment,Category


admin.site.register(Tags)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Category)