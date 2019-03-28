from django.contrib import admin
from .models import Order
import csv
import datetime
from django.http import HttpResponse
# creating generic admin ==> should be before OrderAdmin
def export_to_csv(modeladmin,request,queryset):
    opts = modeladmin.model._meta
    print(opts)
    response = HttpResponse(content_type='text/csv')
    # wait for an attachment
    response['Content-Disposition'] = 'attachment; \
        filename = {}.csv'.format(opts.verbose_name)
    writer = csv.writer(response)
    # exclude m2m and one2m relations
    fields = [field for field in opts.get_fields() if not field.many_to_many and
            not field.one_to_many
        ]
    #write first row with header info
    writer.writerow([field.verbose_name for field in fields])
    #write data rows
    for obj in queryset:
        data_row =[]
        for field in fields:
            value = getattr(obj,field.name)
            if isinstance(value,datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response
export_to_csv.short_description = 'Export to CSV'

class OrderAdmin(admin.ModelAdmin):
    list_display =['id','order_id','status','cart','accepted','date','total']
    list_filter = ['status']
    actions = [export_to_csv]
    #inlines = [] test if child model exist to include on the same page

admin.site.register(Order,OrderAdmin)
