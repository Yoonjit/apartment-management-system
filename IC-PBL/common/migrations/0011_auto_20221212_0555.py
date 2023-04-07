# Generated by Django 3.1.3 on 2022-12-11 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0010_auto_20221210_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=128, unique=True, verbose_name='이메일'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(max_length=128, unique=True, verbose_name='닉네임'),
        ),
    ]
