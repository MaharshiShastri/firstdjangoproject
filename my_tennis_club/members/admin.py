from django.contrib import admin
from .models import Member

class MasterAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date")


admin.site.register(Member, MasterAdmin)