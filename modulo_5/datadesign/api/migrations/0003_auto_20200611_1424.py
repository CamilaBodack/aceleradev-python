# Generated by Django 3.0.6 on 2020-06-11 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200611_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='agent_id',
            new_name='agent',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='groupuser',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='groupuser',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.TextField(max_length=39, validators=[django.core.validators.validate_ipv4_address]),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator]),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator]),
        ),
    ]
