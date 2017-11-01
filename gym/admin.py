from django.contrib import admin

from .models import Member, Registration, Payment, Category
# Register your models here.
admin.site.register(Member)
admin.site.register(Registration)
admin.site.register(Category)
admin.site.register(Payment)