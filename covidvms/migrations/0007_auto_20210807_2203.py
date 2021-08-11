# Generated by Django 3.2.5 on 2021-08-07 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidvms', '0006_rename_id_auth_user_auth_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Auth_user',
        ),
        migrations.AddField(
            model_name='auth',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='auth',
            name='username',
            field=models.CharField(max_length=100, null=True),
        ),
    ]