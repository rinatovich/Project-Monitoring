# Generated by Django 4.1.1 on 2022-10-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0022_delete_note_alter_fielditem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='deadline',
            field=models.DateField(blank=True, null=True, verbose_name='Сроки исполнения'),
        ),
    ]
