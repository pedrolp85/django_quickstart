from django.contrib import admin

from .models import Country

# Register your models here.


class CountryAdmin(admin.ModelAdmin):
    search_fields = ("alpha_code", "numeric_code")
    list_filter = ["alpha_code", "numeric_code"]
    list_display = ["alpha_code", "numeric_code", "name", "region"]


admin.site.register(Country, CountryAdmin)
