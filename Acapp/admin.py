from django.contrib import admin
from .models import Avinyacontact
from .models import Avinyacollab
from .models import AviniyaProject
# Register your models here.

admin.site.register(Avinyacontact)

admin.site .register(Avinyacollab)

@admin.register(AviniyaProject)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'status')
    search_fields = ('name', 'description')
    list_filter = ('status',)
    ordering = ('order',)