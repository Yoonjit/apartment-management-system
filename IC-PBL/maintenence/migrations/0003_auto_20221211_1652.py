# Generated by Django 3.1.3 on 2022-12-11 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenence', '0002_auto_20221211_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenence',
            name='main_date',
            field=models.DateField(primary_key=True, serialize=False),
        ),
    ]