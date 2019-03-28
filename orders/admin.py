from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display =['id','order_id','status','cart','accepted','date','total']
    list_filter = ['status']
    #inlines = [] test if chile model exist to include on the same page

admin.site.register(Order,OrderAdmin)
