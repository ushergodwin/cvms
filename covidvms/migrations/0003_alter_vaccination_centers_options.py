# Generated by Django 3.2.5 on 2021-07-30 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidvms', '0002_auto_20210715_1421'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaccination_centers',
            options={'ordering': ('center_name',)},
        ),
    ]
