from django.contrib import admin

from bankapp.models import District,Branch,Customer


# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name',] #used for admin panel displaying


admin.site.register(District,DistrictAdmin)
admin.site.register(Branch)
admin.site.register(Customer)


