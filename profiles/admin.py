from django.contrib import admin
from .models import BillingProfile

class BillingProfileAdmin(admin.ModelAdmin):
    list_display = ('last_name','email')
    class Meta:
        model = BillingProfile

admin.site.register(BillingProfile,BillingProfileAdmin)
