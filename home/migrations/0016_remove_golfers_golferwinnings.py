# Generated by Django 2.0.2 on 2018-02-10 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20180209_1837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='golfers',
            name='golferwinnings',
        ),
    ]