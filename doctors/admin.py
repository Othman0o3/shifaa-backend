from django.contrib import admin
from django.utils.html import format_html
from .models import Doctor , hospital
# Register your models here.
admin.site.register(Doctor)
@admin.register(hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'safe_location_link')
    fields = ('name', 'address', 'location_link')
    search_fields = ('name', 'address')
    
    def safe_location_link(self, obj):
        if obj.location_link:
            return format_html(
                '<a href="{}" target="_blank" rel="noopener">View on Map</a>',
                obj.location_link
            )
        return "Not provided"
    safe_location_link.short_description = "Map Link"
