# Generated by Django 4.2.3 on 2023-08-26 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.TextField(blank=True),
        ),
    ]