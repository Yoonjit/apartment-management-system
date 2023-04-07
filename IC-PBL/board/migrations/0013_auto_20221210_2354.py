# Generated by Django 3.1.3 on 2022-12-10 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0012_board_mainphoto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='mainphoto',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='board.board')),
            ],
        ),
    ]