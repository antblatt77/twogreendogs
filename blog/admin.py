from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from wagtail.core.models import Page


class PageAdmin(ModelAdmin):
    list_display = ["date", "intro", "body", "page", "depth"]
    list_diaply_links = ["date", "intro", "body", "page", "depth"]
    search_fields = ["intro", "body"]
    raw_id_fields = ["gallery_images"]
    date_hierarchy = ["date"]
    inlines = ["gallery_images"]
    ordering = ["date"]
    fieldsets = [
        ("Blog Content Information:", {"fields": [("date", "intro"), "body"]}),
        ("Blog Gallery Images:", {"fields": [("gallery_images", "caption"), "page"]})
    ]

admin.register(Page, PageAdmin)