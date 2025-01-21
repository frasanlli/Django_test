from django.contrib import admin

from manage_orders.models import Costumers, Items, Orders

# Register your models here.

#To modify which fields are appear on the admin tab of the class, <object table>, we need to create a class with same propertie's name.
#The properties specified will appear, the other ones not
#then the class must be added to the function admin.site.register(<Class to filter>, <Class filter>)
class Admin_costumer(admin.ModelAdmin):
    list_display = ("name","address", "phone")
    search_fields = ("name", "phone")

#To add filters in one side of the admin
class Admin_item(admin.ModelAdmin):
    list_filter=("category",)

#If filtered by date, it is done by time periods
class Admin_order(admin.ModelAdmin):
    list_filter=("number", "date",)
    list_filter=("date",)

admin.site.register(Costumers, Admin_costumer)
admin.site.register(Items, Admin_item)
admin.site.register(Orders, Admin_order)