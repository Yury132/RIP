from django.contrib import admin
from .models import Magnit, Report


class MagnitAdmin(admin.ModelAdmin):
    list_display = ('id','address')
    list_display_links = ('id','address')
    search_fields = ('id','address')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id','magnit_id','quarter', 'profit', 'expense', 'products')
    list_display_links = ('id','magnit_id')

admin.site.register(Magnit, MagnitAdmin)
admin.site.register(Report, ReportAdmin)