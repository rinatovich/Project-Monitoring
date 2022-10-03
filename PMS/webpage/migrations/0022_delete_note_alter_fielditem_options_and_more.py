# Generated by Django 4.1.1 on 2022-10-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0021_project_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.AlterModelOptions(
            name='fielditem',
            options={'ordering': ['id'], 'verbose_name': 'Поля категорий', 'verbose_name_plural': 'Поля категорий'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name': 'Статус', 'verbose_name_plural': 'Статусы'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='executer_company',
        ),
        migrations.AlterField(
            model_name='company',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Название организации'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Имя'),
        ),
        migrations.RemoveField(
            model_name='project',
            name='executor_company',
        ),
        migrations.AddField(
            model_name='project',
            name='executor_company',
            field=models.ManyToManyField(blank=True, null=True, to='webpage.company', verbose_name='Ответстве'),
        ),
    ]