# Generated by Django 2.0.2 on 2018-02-09 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20180209_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='golfers',
            name='teamselection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='golfersel', to='home.Team'),
        ),
    ]
