# Generated by Django 2.1.4 on 2018-12-16 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='qwe',
            field=models.CharField(default='qwe', max_length=12),
        ),
    ]
