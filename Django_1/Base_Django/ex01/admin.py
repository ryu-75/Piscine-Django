from django.contrib import admin
from .models import MarkdownContent

# Create a value for our `MarkdownContent.slug` field based on the value of our title field
class MarkdownContentAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}

admin.site.register(MarkdownContent, MarkdownContentAdmin)
