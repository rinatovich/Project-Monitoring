# Generated by Django 4.0 on 2022-09-22 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0010_alter_project_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
    ]
