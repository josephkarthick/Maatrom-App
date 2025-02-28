from django.contrib import admin
from .models import Slot

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("name", "ph_number", "date", "status", "notes")
    list_filter = ("status", "date")
    search_fields = ("name", "ph_number", "date")
