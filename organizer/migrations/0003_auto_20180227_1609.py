# Generated by Django 2.0.2 on 2018-02-27 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20180227_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='founded_date',
            field=models.DateField(blank=True, null=True, verbose_name='date founded'),
        ),
    ]