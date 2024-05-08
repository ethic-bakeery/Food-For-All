from django.contrib import admin
from .models import User,Payment,UserOrder

admin.site.register(User)
admin.site.register(Payment)
admin.site.register(UserOrder)
