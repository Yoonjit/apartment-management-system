# Generated by Django 3.1.3 on 2022-12-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenence', '0006_auto_20221211_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenence',
            name='id',
            field=models.IntegerField(blank=True, max_length=4, null=True),
        ),
    ]