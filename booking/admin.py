from django.contrib import admin


# Register your models here.
from booking.models import Person, Booking


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Person information', {'fields': ['name', 'contact', 'email']}),
    ]

    list_display = ('name', 'contact', 'email', 'created_on', 'updated_on')

    search_fields = ['name', 'contact', 'email']


class BookingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Person', {'fields': ['person']}),
        ('Booking Details', {'fields': ['description', 'book_dt']}),
    ]

    list_display = ('person', 'book_dt', 'description', 'created_on', 'updated_on')

    search_fields = ['person', 'book_dt', 'description']

    #date_hierarchy = 'book_dt'


admin.site.register(Person, PersonAdmin)
admin.site.register(Booking, BookingAdmin)
