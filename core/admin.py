from django.contrib import admin
from .models import Program, Client, Enrollment

# Program Admin
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name', 'description')

# Client Admin
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'contact_info', 'address')
    search_fields = ('first_name', 'last_name', 'contact_info', 'address')
    list_filter = ('gender',)

# Enrollment Admin
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'program', 'date_enrolled')
    list_filter = ('program', 'date_enrolled')

