from django.contrib import admin

from audioapp.models import   program , subprogram , audio , coupon, OrderDetail
# Register your models he

admin.site.register(program)
admin.site.register(subprogram)
admin.site.register(audio)
admin.site.register(coupon)
admin.site.register(OrderDetail)
