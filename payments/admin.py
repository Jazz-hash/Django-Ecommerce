from django.contrib import admin
from payments.models import Payment, Coupon

# Register your models here.

admin.site.register(Payment)
admin.site.register(Coupon)