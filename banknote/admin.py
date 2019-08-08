from django.contrib import admin
from banknote.models import Person, Appraisal


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on', 'created_by', 'updated_on', 'updated_by')

    list_display = ('name', 'contact', 'email', 'created_on', 'updated_on')

    search_fields = ['name', 'contact', 'email']

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


class AppraisalAdmin(admin.ModelAdmin):

    readonly_fields = ('created_on', 'created_by', 'updated_on', 'updated_by')

    list_display = ('id_num', 'country', 'series', 'grading', 'variety')

    search_fields = ['id_num', 'country', 'series', 'grading']

    def save_model(self, request, obj, form, change):
        if not obj.created_by_id:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.appraiser = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Person, PersonAdmin)
admin.site.register(Appraisal, AppraisalAdmin)
