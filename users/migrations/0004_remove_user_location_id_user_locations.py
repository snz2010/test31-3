# Generated by Django 4.0.5 on 2022-06-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_location_id_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='location_id',
        ),
        migrations.AddField(
            model_name='user',
            name='locations',
            field=models.ManyToManyField(to='users.location'),
        ),
    ]
