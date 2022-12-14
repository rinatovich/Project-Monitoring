# Generated by Django 4.0 on 2022-09-19 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0003_alter_project_primary_manager_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='executer_company_secondary',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary', to='webpage.company', verbose_name='secondary company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='executer_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_company', to='webpage.company', verbose_name='prime company'),
        ),
    ]
