# Generated by Django 4.1.1 on 2022-09-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0016_remove_project_statusfield_project_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Указание',
                'verbose_name_plural': 'Указания',
            },
        ),
    ]