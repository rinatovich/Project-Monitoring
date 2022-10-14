# Generated by Django 4.1.1 on 2022-10-14 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0026_note_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='activities',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Мероприятия'),
        ),
        migrations.AddField(
            model_name='project',
            name='finance',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Финансовые вопросы'),
        ),
        migrations.AddField(
            model_name='project',
            name='problems',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Проблемные вопросы'),
        ),
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Состояние'),
        ),
        migrations.AddField(
            model_name='project',
            name='system',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Система'),
        ),
    ]
