# Generated by Django 2.1.5 on 2019-11-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0003_auto_20191106_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='room',
            field=models.IntegerField(default=None),
        ),
    ]
