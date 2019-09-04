from django.contrib import admin
from django.contrib.admin.options import ModelAdmin


class BlogAdmin(ModelAdmin):
    list_display = ["date", "intro", "body", "page"]
    list_diaply_links = ["page"]
    search_fields = ["intro", "body"]
    date_hierarchy = ["date"]
    inlines = ["gallery_images"]
    ordering = ["date"]
    fieldsets = [
        ("Blog Content Information:", {"fields": [("date", "intro"), "body"]}),
        ("Blog Gallery Images:", {"fields": [("gallery_images", "caption"), "page"]})
    ]
