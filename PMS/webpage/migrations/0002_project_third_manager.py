# Generated by Django 4.0 on 2022-09-19 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='third_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='third_manager', to='webpage.manager', unique=True, verbose_name='third manager'),
        ),
    ]
