# Generated by Django 4.0 on 2022-09-21 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpage', '0005_alter_company_options_alter_manager_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Категория',
            },
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['id'], 'verbose_name': 'Проекты', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='project',
            name='executer_company',
            field=models.ManyToManyField(to='webpage.Company', verbose_name='Ответстве'),
        ),
        migrations.AlterField(
            model_name='project',
            name='manager',
            field=models.ManyToManyField(to='webpage.Manager', verbose_name='Менеджеры'),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webpage.category', verbose_name='Категория'),
        ),
    ]
