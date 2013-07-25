from django.contrib import admin
from .models import Contact
from .models import Note
from .models import Phone

class NoteInline(admin.StackedInline):
	model = Note
	extra = 1

class PhoneInline(admin.TabularInline):
	model = Phone
	extra = 1

class ContactAdmin(admin.ModelAdmin):
	model = Contact
	list_display = ['first_name', 'last_name', 'useful_email']
	search_fields = ['first_name', 'last_name', 'email']
	ordering = ['last_name','first_name']
	list_filter = ['active']
	list_display_links =['first_name','last_name']
	inlines = [NoteInline, PhoneInline]

admin.site.register(Contact,ContactAdmin)

	

