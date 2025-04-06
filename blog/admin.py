from django.contrib import admin
from  .models import BlogPost

# Register your models here.

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'featured_image', 'published')
        }),
        ('SEO Options', {
            'classes': ('collapse',),
            'fields': ('seo_title', 'seo_description', 'canonical_url', 'noindex')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at')
        }),
    )
    readonly_fields = ('created_at', 'updated_at')