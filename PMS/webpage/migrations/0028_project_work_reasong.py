# Generated by Django 4.1.1 on 2022-10-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0027_project_activities_project_finance_project_problems_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='work_reasong',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Основания для выполнения работ'),
        ),
    ]
