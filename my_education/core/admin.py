from django.contrib import admin
from .models import Page, Person

class PersonInline(admin.StackedInline):
    model = Person
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('role', 'full_name', 'photo', 'email', 'phone', 'resume', 'description')
        }),
    )

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'nav_title', 'priority', 'show_in_nav')
    list_editable = ('priority', 'show_in_nav')
    list_filter = ('show_in_nav',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PersonInline]