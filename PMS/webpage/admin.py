from django.contrib import admin
from import_export.fields import Field

from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources
from import_export import fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget


# Register your models here.
class ProjectResource(resources.ModelResource):
    manager = fields.Field(column_name='Менеджер', attribute='manager',
                           widget=ForeignKeyWidget(Manager, 'name'))
    executer_company = fields.Field(column_name='Исполняющая организация', attribute='executer_company',
                                    widget=ForeignKeyWidget(Company, 'title'))
    list_display = [field.name for field in Project._meta.fields]
    title = Field(attribute='title', column_name='Наименование объекта')
    work_statement = Field(attribute='wordk_statement', column_name='Описание работ')
    contract_id = Field(attribute='contract_id', column_name='Номер договора')
    note = Field(attribute='note', column_name='Примечание')
    customer = Field(attribute='customer', column_name='Заказчик')
    status = Field(attribute='customer', column_name='Статус')
    cat = fields.Field(column_name='Категория', attribute='cat',
                       widget=ForeignKeyWidget(Category, 'title'))
    deadline = Field(attribute='deadline', column_name='Срок исполнения')

    class Meta:
        model = Project
        fields = [field.name for field in Project._meta.fields]
        export_order = [field.name for field in Project._meta.fields]


class ProjectAdmin(ImportExportActionModelAdmin):
    resource_class = ProjectResource
    list_display = [field.name for field in Project._meta.fields]
    list_display_links = ('title',)
    search_fields = ('title',)
    ordering = ('id',)
    list_filter = ('cat',)
    filter_horizontal = ['manager', 'executer_company']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['fields']


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Manager,ManagerAdmin)
admin.site.register(Company)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(FieldItem)
admin.site.register(Status)
