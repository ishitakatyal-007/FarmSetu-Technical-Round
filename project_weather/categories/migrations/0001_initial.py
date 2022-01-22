# Generated by Django 3.2.11 on 2022-01-18 12:27

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('category_id', models.AutoField(help_text='Unique ID for category', primary_key=True, serialize=False, verbose_name='Category ID')),
                ('category_name', models.CharField(help_text='Name of Category', max_length=100, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ('category_name',),
            },
        ),
    ]