from django.contrib import admin
from .models import Category, Region, Localite, Commodite, Immobilier, ImmageDB, Service, Vendor, Client, ClientAlert


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class ImmobilierAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('region',)}


class LocaliteAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('localite',)}


class CommoditeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class VendorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Immobilier, ImmobilierAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Localite, LocaliteAdmin)
admin.site.register(Commodite, CommoditeAdmin)
admin.site.register(ImmageDB)
admin.site.register(Service)
admin.site.register(Vendor)
admin.site.register(Client)
admin.site.register(ClientAlert)