# Generated by Django 4.0 on 2022-09-19 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.FileField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('work_statement', models.TextField(blank=True, null=True)),
                ('contract_id', models.CharField(blank=True, max_length=250, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('customer', models.CharField(blank=True, max_length=250, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('executor_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webpage.company')),
                ('primary_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_manager', to='webpage.manager', unique=True, verbose_name='Primary manager')),
                ('secondary_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_manager', to='webpage.manager', unique=True, verbose_name='secondary manager')),
            ],
        ),
    ]
