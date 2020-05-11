# Generated by Django 3.0.6 on 2020-05-11 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(editable=False, max_length=30, unique=True),
        ),
    ]