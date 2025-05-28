from django.contrib import admin

# Register your models here.
from .models import Subscribe, Partner, Contact, ContactUs

admin.site.register(Subscribe)
admin.site.register(Partner)
admin.site.register(Contact)
admin.site.register(ContactUs)
