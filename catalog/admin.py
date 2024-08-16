from django.contrib import admin
from django import forms
from .models import Author, Genre, Book, BookInstance, Language
from django.forms import ModelForm
# Register your models here.


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

class BookInstanceForm(ModelForm):
    class Meta:
        widgets = {
            "status": forms.Select(
                attrs={
                    # all hidden by default
                    "--hideshow-fields": 'sales_date',
                    # a2, a4 visible when "0" is selected
                    "--show-on-o": "sales_date",
                    # a1, a2 visible when "1" is selected
                    #"--show-on-1": "a1, a2",
                }
            ),
        }

    class Media:
        js = ("hideshow.js",)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death'), 'short_biography']
class BookInstanceAdmin(admin.ModelAdmin):
    form = BookInstanceForm
    list_display = ('book', 'id', 'status')
    list_filter = ['status']
    fieldsets = (
        (None, {
            'fields':('book', 'id')
        }),
        ('Availability', {
            'fields':('status', 'sales_date')
        }),
    )
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'display_language')
    inlines = [BooksInstanceInline]
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book,BookAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language)
