from django.contrib import admin
from .models import PetMemorial, PetMemorialGalleryImage, CandleMessage


# Inline gallery image uploader inside PetMemorial edit form
class PetMemorialGalleryImageInline(admin.TabularInline):
    model = PetMemorialGalleryImage
    extra = 1  # Show 1 empty image slot by default

class CandleMessageInline(admin.TabularInline):
    model = CandleMessage
    extra = 1  # Show 1 empty candle row by default


# Admin for PetMemorial (main model)
@admin.register(PetMemorial)
class PetMemorialAdmin(admin.ModelAdmin):
    list_display = ("pet_name", "species", "user", "year_of_birth", "year_of_death")
    search_fields = ("pet_name", "user__username", "species", "breed")
    list_filter = ("species", "year_of_death")
    ordering = ("-year_of_death",)
    inlines = [PetMemorialGalleryImageInline, CandleMessageInline]


# Optional: Admin for gallery images themselves
@admin.register(PetMemorialGalleryImage)
class PetMemorialGalleryImageAdmin(admin.ModelAdmin):
    list_display = ("pet_memorial", "caption", "image")
    search_fields = ("caption", "pet_memorial__pet_name")
    list_filter = ("pet_memorial",)
