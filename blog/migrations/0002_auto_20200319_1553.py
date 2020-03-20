# Generated by Django 3.0.3 on 2020-03-19 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagedescription',
            name='media/logo.png',
        ),
        migrations.AddField(
            model_name='pagedescription',
            name='photo',
            field=models.ImageField(default='logo.png', upload_to='pageImg'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='logo.png', upload_to='posts'),
        ),
    ]