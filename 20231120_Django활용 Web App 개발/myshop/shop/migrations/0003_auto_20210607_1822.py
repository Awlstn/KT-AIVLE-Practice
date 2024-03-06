# Generated by Django 2.1 on 2021-06-07 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20210607_1802'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('id',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.CharField(db_index=True, max_length=200, primary_key=True, serialize=False),
        ),
    ]
