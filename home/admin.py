from django.contrib import admin

class HomePageAdmin(admin.StackedInline):
    fields = "__all__"
